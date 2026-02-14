import json
import re

def extract_strings(data):
    # Set to store unique strings to avoid redundant translations
    to_translate = set()
    
    def traverse(obj):
        if isinstance(obj, dict):
            if obj.get('type') in ['AboutText', 'Translate']:
                content = obj.get('content', '').strip()
                if content:
                    to_translate.add(content)
            for value in obj.values():
                traverse(value)
        elif isinstance(obj, list):
            for item in obj:
                traverse(item)

    traverse(data)
    return sorted(list(to_translate))

def main():
    try:
        with open('chapters.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        strings = extract_strings(data)
        
        # Save unique strings to a file for analysis
        with open('strings_to_translate.txt', 'w', encoding='utf-8') as f:
            for s in strings:
                f.write(s.replace('\n', '\\n') + '\n')
        
        print(f"Extracted {len(strings)} unique strings for translation.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
