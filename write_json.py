import config
import json
import time
import os

def write_json(data: dict = None, path: str=config.DEFAULT_OUTPUT_PATH):
    """Запись в данных в JSON"""
    try:
        json_object = json.dumps(data,indent=4,ensure_ascii=False)

        filename = f'{(int(time.time()))}result.json'
        filepath = os.path.join(path, filename)

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(filepath, 'w+', encoding='utf-8') as outfile:
            outfile.write(json_object)

        return filepath
    except Exception as e:
        print(e)
