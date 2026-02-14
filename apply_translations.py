import json
import os

def update_json(mapping_file, source_json, target_json):
    with open(mapping_file, 'r', encoding='utf-8') as f:
        mapping = json.load(f)
    
    with open(source_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    def traverse(obj):
        if isinstance(obj, dict):
            if obj.get('type') in ['AboutText', 'Translate']:
                content = obj.get('content', '').strip()
                if content in mapping:
                    obj['content'] = mapping[content]
            for key, value in obj.items():
                if key == 'title' and isinstance(value, str):
                    if value.strip() in mapping:
                        obj[key] = mapping[value.strip()]
                traverse(value)
        elif isinstance(obj, list):
            for item in obj:
                traverse(item)

    traverse(data)
    
    with open(target_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_json('translations.json', 'chapters.json', 'chapters_urdu.json')
