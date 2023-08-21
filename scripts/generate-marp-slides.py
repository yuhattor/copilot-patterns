import os
import re
import yaml
import argparse


FOOTER_PREFIX = "GitHub Copilot Patterns"

# Define section input patterns as a constant
SECTION_PATTERNS = [
    ('top', r'## (.+?)\n(?=### Description)'),
    ('description', r'### Description\n\n(.*?)(###|####|\Z)'),
    ('example', r'#### Example\n\n(.*?)(###|\Z)'),
    ('exercise', r'### Exercise\n\n(.*?)(###|\Z)'),
    ('checklist', r'### Checklist for Further Learning\n\n(.*?)(###|\Z)'),
]

# Define section output config as a constant
SECTION_CONFIG = {
    'top': {"class": "top", "head": "{title}"},
    'description': {"class": "description",  "head": "Description"},
    'example': {"class": "example",  "head": "Example"},
    'exercise': {"class": "exercise",  "head": "Exercise"},
    'checklist': {"class": "checklist",  "head": "Checklist for Further Learning"}
}

# Define the level mapping
LEVEL_MAPPING = {
    "lv0": {"name": "Pattern_Idea", "color": "blueviolet"},
    "lv1": {"name": "Early_Stage_Pattern", "color": "blue"},
    "lv2": {"name": "Practically_Viable_Pattern", "color": "green"},
    "lv3": {"name": "Mature_Best_Practice", "color": "brightgreen"}
}

# Define the order of the category
CATEGORY_ORDER = [
    "general", 
    "client-tips", 
    "design-pattern", 
    "collaboration", 
    "testing", 
    "refactoring"
]

def parse_args():
    parser = argparse.ArgumentParser(description="Generate document.")
    parser.add_argument('--sections', nargs='+', default=['top', 'description', 'example', 'exercise', 'checklist'], help="Sections to include in the final document.")
    parser.add_argument('--levels', nargs='+', default=['lv0', 'lv1', 'lv2', 'lv3'], help="Levels to include in the final document.")
    parser.add_argument('--locale', default='en', choices=['en', 'ja'], help="Locale to specify the root directory.")

    return parser.parse_args()

def _extract_section(pattern, content):
    """Helper function to extract a section using a given pattern."""
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else None

def extract_sections(content):
    """ Extracts sections from the provided content using predefined patterns."""
    return {title: _extract_section(pattern, content) for title, pattern in SECTION_PATTERNS if _extract_section(pattern, content)}

def extract_yaml(content):
    """ Extracts YAML content from the provided string."""
    pattern = r'---\n(.*?)\n---'
    match = re.search(pattern, content, re.DOTALL)
    return yaml.safe_load(match.group(1)) if match else {}

def read_file_content(file_path):
    """Read the content of the given file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def parse_file_content(content):
    """Parse sections and YAML content from the given file content."""
    sections = extract_sections(content)
    meta = extract_yaml(content)
    meta["short-description"] = meta.get("description", "")
    return {**meta, **sections}

def read_and_parse_files(directory, levels):

    """Read and parse markdown files from the specified directory."""
    parsed_contents = []

    for subdir, _, files in os.walk(directory):
        if subdir != directory:  # process only root directory contents
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(subdir, file)
                    content = read_file_content(file_path)
                    parsed_contents.append(parse_file_content(content))
    
    ## Sort the parsed contents by the CATEGORY_ORDER and then by the LEVEL_MAPPING in the descending order
    parsed_contents.sort(key=lambda x: (CATEGORY_ORDER.index(x["category"]), -int(x["level"][2:])))
    # Filter parsed_contents by level
    parsed_contents = [content for content in parsed_contents if content.get("level") in levels]
    return parsed_contents

def extract_hint_content(hint):
    """Extract the content inside a specific hint tag and format it."""
    pattern = r'{% hint style="info" %}\n(.*?)\n{% endhint %}'
    match = re.search(pattern, hint, re.DOTALL)
    if match:
        return '> ' + '\n> '.join(match.group(1).strip().split('\n'))
    return None

def clean_content(content, section):
    target_content = content[section]
    """Clean and transform the given content."""
    # Modify image links to a simpler markdown format
    target_content = re.sub(r'\[<img src="(.*?)">\]\(.*?\)', r'![](\1)', target_content)
    # Remove the first line
    if section == "top":
        target_content = re.sub(r'^.*?\n', '', target_content)
        # Extract content from a specific hint tag
        hint_content = extract_hint_content(target_content)
        # Remove the original hint tag and its content
        target_content = re.sub(r'{% hint style="info" %}.*?{% endhint %}', '', target_content, flags=re.DOTALL)
        # Append the formatted hint content, if it exists
        if hint_content:
            target_content += '\n\n' + hint_content
    return target_content.strip()


def format_marp_section(class_name, header, head, content, section, title):
    
    # Customize Functions Mapping
    customize_functions = {
        "top": customize_top_section
    }
    
    content[section] = clean_content(content, section)
    customize_func = customize_functions.get(section, customize_default_section)
    content_section = customize_func(content, section, head)
    
    header_elements = {
        "_class": f"{class_name}",
        "_footer": f"{FOOTER_PREFIX} - {title}",
        "_header": header
    }
    
    header_section = "<!-- \n"
    for key, value in header_elements.items():
        header_section += f"{key}: \"{value}\"\n"
    header_section += "-->\n"

    return header_section + content_section

def generate_category_slide(parsed_contents, category):
    titles = [f"- {content['title']}\n" for content in parsed_contents if content["category"] == category]
    title_list = "".join(titles)
    return f"<!-- _class: example -->\n## {category.replace('-', ' ').capitalize()}\n\n{title_list}\n\n---\n"

def generate_section_slide(section, config, content, title, category_name):
    head = config["head"].format(title=title)
    return format_marp_section(config["class"], category_name, head, content, section, title)

def generate_ending_slide():
    return f"<!-- _class: top -->\n# Thank you\n\n"

def convert_to_marp(parsed_contents, sections):
    """Convert the parsed contents to Marp format."""
    marp_content = ""
    last_category = ""

    for content in parsed_contents:
        title = content.get("title", "")
        category = content.get("category", "")
        category_name = " ".join([word.capitalize() for word in category.replace("-", " ").split(" ")])

        if last_category != category or not last_category:
            marp_content += generate_category_slide(parsed_contents, category)

        for section, config in SECTION_CONFIG.items():
            if section in content and content[section] and section in sections:
                marp_content += generate_section_slide(section, config, content, title , category_name)

        last_category = category

        if content == parsed_contents[-1]:
            marp_content += generate_ending_slide()

    return marp_content

def customize_top_section(content, section, category):
    cleaned_content = f"{content['short-description']}\n\n{content[section]}"
    return f"## {category}\n\n{cleaned_content}\n\n---\n"

def customize_default_section(content, section, category):
    cleaned_content = f"## {content['title']}\n\n{content[section]}"

    # Insert title to the second line of cleaned_content
    content_section = cleaned_content.split("\n", 1)
    content_section.insert(1, f"\n\n### {category}\n\n")
    return "".join(content_section) + "\n\n---\n"

def main():
    args = parse_args()
    sections_to_include = args.sections
    levels_to_include = args.levels
    locale = args.locale

    root_dir = f'contents/{locale}/'  # Set ROOT_DIR based on the locale
    contents = read_and_parse_files(root_dir, levels_to_include)

    # Add marp_content to scripts/base-docs.md and save it as ./output_marp.md
    with open(f"scripts/base-docs.{locale}.md", "r", encoding="utf-8") as f:
        base_docs = f.read()
        marp_content = base_docs + convert_to_marp(contents, sections_to_include)
    with open(f"output_marp.{locale}.md", "w", encoding="utf-8") as f:
        f.write(marp_content)

if __name__ == '__main__':
    main()
