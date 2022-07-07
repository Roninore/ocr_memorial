#Libraries
import glob
import easyocr
import time
import os
from GPSPhoto import gpsphoto

#Files
import config
from validation.parse_raw_result import parse_raw_result

def read_dir(dir_path: str=config.DEFAULT_INPUT_PATH, file_types: tuple=('jpg','png','jpeg')) -> list:
    """Возвращает массив ответов с фотографий.\n
    если необходимо обрабатывать сразу много фоток, то лучше использовать эту функцию, она
    создает easyocr.Reader один раз, а не делает это для каждой фотки (-6 секунд на обработку фотки)"""

    files = get_files_from_dir(dir_path,file_types) 
    
    # Логирование того, сколько файлов найдено
    if len(files): 
        print(f'Finded {len(files)} files in {dir_path}, starting to create reader..')
    else:
        print((f'Finded {len(files)} files in {dir_path}, finish..'))
        return
    
    start_time = time.time() # Таймер на лог о времени создания ридера
    reader = easyocr.Reader(lang_list=config.OCR_LANG_LIST,gpu=config.OCR_GPU) # Создаем ридер

    print('Start reading.. ' + '({:.2f}s. to create reader)'.format(time.time() - start_time))

    # Последовательно обрабатываем каждую нужну фотографию
    # и вносим в результирующий массив
    answer = [] 
    for file in files:
        answer.append(read_photo_easyocr(path=file,reader=reader))
    
    return answer


def get_files_from_dir(dir_path: str=config.DEFAULT_INPUT_PATH, file_types: tuple=('jpg','png','jpeg')) -> list:
    """Получить пути к файлам из директории"""

    # Последовательно для каждого подходящего типа добавляем файлы в общий массив
    files = []
    for ft in file_types:
        files.extend(glob.glob(dir_path +'*.' + ft))
    
    return files
    
    
def read_photo_easyocr(path: str, reader:easyocr.Reader = None) -> dict:
    """Прочитать изображение через Easy OCR"""    
    try:
        # Если ридер не передали в функцию - создаем новый
        if not reader:
            reader = easyocr.Reader(lang_list=config.OCR_LANG_LIST,gpu=config.OCR_GPU)
    
        filename = os.path.basename(path) # Имя без пути, для результата
    
        start_time = time.time() # Таймер на чтение текста и читаем текст с фотографии
        raw_result = reader.readtext(path,detail=0,paragraph=True,add_margin=0.1,adjust_contrast=0.8)

        result = parse_raw_result(raw_result) # Преобразуем список абзацов в нужный формат
        
        GPSdata = gpsphoto.getGPSData(path) # Геометки фотографии

        return {'data': result, # Данные о прочитанном тексте
                'filename': filename, # Название файла
                'gps': GPSdata, # Геометки
                'time': '{:.2f}s.'.format(time.time() - start_time)} # Время на обработку фотографии

    except Exception as e:
        print(e)
        return {
                'data': {'full_name': '',
                         'years': '',
                         'filename': filename },
                'gps': {'Latitude':'',
                        'Longitude':''},
                'time': '0' }



