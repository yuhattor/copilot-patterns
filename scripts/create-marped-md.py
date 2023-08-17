import os
import re
import yaml
from pprint import pprint

root_dir = 'contents/en'

def extract_sections(content):
    section_patterns = [
        ('title', r'## (.+?)\n(?=### Description)'),  # Lookahead assertionを追加して、次のセクションまでの内容をキャプチャしないようにします
        ('description', r'### Description\n\n(.*?)(###|####|\Z)'),
        ('example', r'#### Example\n\n(.*?)(###|\Z)'),
        ('exercise', r'### Exercise\n\n(.*?)(###|\Z)'),
        ('checklist', r'### Checklist for Further Learning\n\n(.*?)(###|\Z)'),
    ]

    sections = {}
    for name, pattern in section_patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            sections[name] = match.group(1).strip()

    return sections

def extract_yaml(content):
    pattern = r'---\n(.*?)\n---'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return yaml.safe_load(match.group(1))
    return {}

def read_and_parse_files(directory):
    parsed_contents = []
    
    for subdir, _, files in os.walk(directory):
        # skip if the contents is not in the root directory
        if subdir == directory:
            continue
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    sections = extract_sections(content)
                    meta = extract_yaml(content)
                    meta["short-description"] = meta["description"]
                    parsed_content = {**meta, **sections}
                    parsed_contents.append(parsed_content)

    return parsed_contents

def extract_hint_content(hint):
    pattern = r'{% hint style="info" %}\n(.*?)\n{% endhint %}'
    match = re.search(pattern, hint, re.DOTALL)
    if match:
        return '> ' + '\n> '.join(match.group(1).strip().split('\n'))
    return None

def clean_content(content):
    # 画像のリンクを変更
    content = re.sub(r'\[<img src="(.*?)">\]\(.*?\)', r'![](\1)', content)
    # 先頭行を削除
    content = re.sub(r'^.*?\n', '', content)

    # content = re.sub(r'## .*?\n', '', content)
    # 特定のヒントの内容を抜き出す
    hint_content = extract_hint_content(content)
    
    # ヒントの内容を元の内容から削除
    content = re.sub(r'{% hint style="info" %}.*?{% endhint %}', '', content, flags=re.DOTALL)
    
    # ヒント内容が存在すれば追加
    if hint_content:
        content += '\n\n' + hint_content
    
    return content.strip()



def convert_to_marp(parsed_contents):
    marp_content = ""

    for content in parsed_contents:
        name = clean_content(content['name'])

        if 'title' in content and content['title']:
            marp_content += f"<!-- \nclass: title \nfooter: \"GitHub Copilot Patterns\"\nheader: \"{name}\"\n-->\n## {clean_content(content['name'])} \n\n{clean_content(content['short-description'])} \n\n{clean_content(content['title'])}\n\n---\n"

            pprint(clean_content(content['title']))


        
        if 'description' in content and content['description']:
            marp_content += f"<!-- \nclass: description \nfooter: \"GitHub Copilot Patterns - {name}\"\nheader: \"Description\"\n-->\n## Description\n\n{clean_content(content['description'])}\n\n---\n"
        
        if 'example' in content and content['example']:
            marp_content += f"<!-- \nclass: example \nfooter: \"GitHub Copilot Patterns - {name}\"\nheader: \"Example\"\n-->\n## Example\n\n{clean_content(content['example'])}\n\n---\n"
        
        if 'exercise' in content and content['exercise']:
            marp_content += f"<!-- \nclass: exercise \nfooter: \"GitHub Copilot Patterns - {name}\"\nheader: \"Exercise\"\n-->\n## Exercise\n\n{clean_content(content['exercise'])}\n\n---\n"
        
        if 'checklist' in content and content['checklist']:
            marp_content += f"<!-- \nclass: checklist \nfooter: \"GitHub Copilot Patterns - {name}\"\nheader: \"Checklist for Further Learning\"\n-->\n## Checklist for Further Learning\n\n{clean_content(content['checklist'])}\n\n---\n"

    return marp_content



def main():
    contents = read_and_parse_files(root_dir)
    marp_content = convert_to_marp(contents)
    
    # 出力
    with open("output_marp.md", "w", encoding="utf-8") as f:
        f.write(marp_content)

if __name__ == '__main__':
    main()