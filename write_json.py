import config
import json
import time
import os

def write_json(data: dict = None, path: str=config.DEFAULT_OUTPUT_PATH) -> str:
    """Запись в данных в JSON, возвращает путь к результирующему файлу"""
    try:
        json_object = json.dumps(data,indent=4,ensure_ascii=False) # Создаем JSON фрагмент

        filename = f'{(int(time.time()))}result.json' # Генерируем имя файла (через таймштамп)
        filepath = os.path.join(path, filename) # Путь к файлу

        os.makedirs(os.path.dirname(path), exist_ok=True) # Создаем папки (если первый раз записываем в стандартную директорию)

        with open(filepath, 'w+', encoding='utf-8') as outfile: # Запись в файл
            outfile.write(json_object)

        return filepath
        
    except Exception as e:
        print(e)
