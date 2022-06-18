# Конфигурация и константы
import os.path as path
import os


ROOT_DIR = path.dirname(path.abspath(__file__)) # Корневая папка проекта
DEFAULT_INPUT_PATH = path.join(ROOT_DIR,'input') # Стандартная папка ввода
DEFAULT_OUTPUT_PATH = path.join(ROOT_DIR, 'output') # Стандартная папка вывода

NAMES_PATH = path.join(ROOT_DIR + '/validation/data/' + 'russian_names.json') # База имен
SURNAMES_PATH = path.join(ROOT_DIR + '/validation/data/' + 'russian_surnames.json') # База фамалий
PATRONYMIC_PATH = path.join(ROOT_DIR + '/validation/data/' + 'patronymic.json') # База отчеств

os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:256' # Значение для CUDA (предотвращение переполнения видеопамяти)
OCR_GPU = True # Использовать ли GPU в распознании
OCR_LANG_LIST = ['ru'] # Список распознаваемых языков