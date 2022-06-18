#Libraries
import glob
import easyocr
import time
import os

#Files
import config
from validation.parse_raw_result import parse_raw_result

def read_dir(dir_path: str=config.DEFAULT_INPUT_PATH, file_types: tuple=('jpg','png','jpeg')):
    """Возвращает массив ответов с фотографий"""

    files = get_files_from_dir(dir_path,file_types)
    
    if len(files):
        print(f'Finded {len(files)} files in {dir_path}, starting to create reader..')
    else:
        print((f'Finded {len(files)} files in {dir_path}, finish..'))
        return
    
    start_time = time.time()
    reader = easyocr.Reader(lang_list=config.OCR_LANG_LIST,gpu=config.OCR_GPU)

    print('Start reading.. ' + '({:.2f}s. to create reader)'.format(time.time() - start_time))

    answer = [] 
    for file in files:
        answer.append(read_photo_easyocr(path=file,reader=reader))
    
    return answer


def get_files_from_dir(dir_path: str=config.DEFAULT_INPUT_PATH, file_types: tuple=('jpg','png','jpeg')):
    """Получить пути к файлам из директории"""

    files = []
    for ft in file_types:
        files.extend(glob.glob(dir_path +'\*.' + ft))
    
    return files
    
    
def read_photo_easyocr(path, reader:easyocr.Reader = None):
    """Прочитать изображение через Easy OCR"""
    if not reader:
        reader = easyocr.Reader(lang_list=config.OCR_LANG_LIST,gpu=config.OCR_GPU)
    
    filename = os.path.basename(path)
    try:
        start_time = time.time()
        raw_result = reader.readtext(path,detail=0,paragraph=True,add_margin=0.1,adjust_contrast=0.8)

        result = parse_raw_result(raw_result)
        
        return {'data' : result,'filename':filename, 'time' : '{:.2f}s.'.format(time.time() - start_time)}
    except Exception as e:
        print(e)
        return {'data': {'full_name':'','years':'','filename':filename}, 'time': '0'}



    



