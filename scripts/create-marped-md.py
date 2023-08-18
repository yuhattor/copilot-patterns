import os
import re
import yaml
from pprint import pprint

# Define the root directory of the contents
ROOT_DIR = 'contents/en'

# Define section input patterns as a constant
SECTION_PATTERNS = [
    ('title', r'## (.+?)\n(?=### Description)'),
    ('description', r'### Description\n\n(.*?)(###|####|\Z)'),
    ('example', r'#### Example\n\n(.*?)(###|\Z)'),
    ('exercise', r'### Exercise\n\n(.*?)(###|\Z)'),
    ('checklist', r'### Checklist for Further Learning\n\n(.*?)(###|\Z)'),
]

# Define section output config as a constant
SECTION_CONFIG = {
    'title': {"class": "title", "footer_prefix": "GitHub Copilot Patterns", "header": "", "title": "{name}"},
    'description': {"class": "description", "footer_prefix": "GitHub Copilot Patterns", "header": "Description", "title": "Description"},
    'example': {"class": "example", "footer_prefix": "GitHub Copilot Patterns", "header": "Example", "title": "Example"},
    'exercise': {"class": "exercise", "footer_prefix": "GitHub Copilot Patterns", "header": "Exercise", "title": "Exercise"},
    'checklist': {"class": "checklist", "footer_prefix": "GitHub Copilot Patterns", "header": "Checklist for Further Learning", "title": "Checklist for Further Learning"}
}

def _extract_section(pattern, content):
    """Helper function to extract a section using a given pattern."""
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else None

def extract_sections(content):
    """ Extracts sections from the provided content using predefined patterns."""
    return {name: _extract_section(pattern, content) for name, pattern in SECTION_PATTERNS if _extract_section(pattern, content)}

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

def read_and_parse_files(directory):
    """Read and parse markdown files from the specified directory."""
    parsed_contents = []

    for subdir, _, files in os.walk(directory):
        if subdir != directory:  # process only root directory contents
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(subdir, file)
                    content = read_file_content(file_path)
                    parsed_contents.append(parse_file_content(content))

    return parsed_contents

def extract_hint_content(hint):
    """Extract the content inside a specific hint tag and format it."""
    pattern = r'{% hint style="info" %}\n(.*?)\n{% endhint %}'
    match = re.search(pattern, hint, re.DOTALL)
    if match:
        return '> ' + '\n> '.join(match.group(1).strip().split('\n'))
    return None

def transform_content(content):
    """Clean and transform the given content."""
    # Modify image links to a simpler markdown format
    content = re.sub(r'\[<img src="(.*?)">\]\(.*?\)', r'![](\1)', content)
    # Remove the first line
    content = re.sub(r'^.*?\n', '', content)
    # Extract content from a specific hint tag
    hint_content = extract_hint_content(content)
    # Remove the original hint tag and its content
    content = re.sub(r'{% hint style="info" %}.*?{% endhint %}', '', content, flags=re.DOTALL)
    # Append the formatted hint content, if it exists
    if hint_content:
        content += '\n\n' + hint_content
    return content.strip()


def format_marp_section(class_name, footer_prefix, header, title, content, name):
    """Generate the Marp-formatted section."""
    cleaned_content = transform_content(content)
    return (f"<!-- \nclass: {class_name} \nfooter: \"{footer_prefix} - {name}\"\n"
            f"header: \"{header}\"\n-->\n## {title}\n\n{cleaned_content}\n\n---\n")

def convert_to_marp(parsed_contents):
    """Convert the parsed contents to Marp format."""
    marp_content = ""
    for content in parsed_contents:
        name = transform_content(content['name'])
        for section, config in SECTION_CONFIG.items():
            if section in content and content[section]:
                title = config["title"].format(name=name)
                marp_content += format_marp_section(config["class"], config["footer_prefix"], config["header"], title, content[section], name)
                if section == 'title':
                    pprint(transform_content(content['title']))
    return marp_content

def main():
    contents = read_and_parse_files(ROOT_DIR)
    marp_content = convert_to_marp(contents)
    with open("output_marp.md", "w", encoding="utf-8") as f:
        f.write(marp_content)

if __name__ == '__main__':
    main()
