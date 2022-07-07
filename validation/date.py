#Libraries
import re
from datetime import date


def get_dates(raw_string: str='') -> dict:
    """Получить отформатированные даты"""
    try:
        answ = re.sub(r'[^0-9.]',' ',raw_string).strip() # Оставляем только цифры
        answ = re.sub(r'\s+',' ',answ) # Удаляем двойные пробелы

        match = re.match(r'(\d{2}\.\d{2}\.\d{4}).*(\d{2}\.\d{2}\.\d{4})',answ)
        if match:  #Если дата в стандартном виде (dd.mm.yyyy dd.mm.yyyy)
            return {'left': match.group(1),'right': match.group(2),'raw': answ}

        match = re.match(r'.*(\d{2})[0-9\s]+(\d{2}).*(\d{2}).*(\d{2}).*', answ)
        if match: #Если дата в виде yyyy - yyyy
            return validate_date(left=match.group(1)+match.group(2),right=match.group(3)+match.group(4),raw=answ)

        return {'left': '', 
                'right': '', 
                'raw': answ}
    except:
        return {'left': '', 
                'right': '', 
                'raw': raw_string}


def validate_date(left:str,right:str,raw:str) -> dict:
    """Проверить дату формата yyyy-yyyy"""
    # Границы возможных дат
    MIN_YEAR = 1500 
    MAX_YEAR = date.today().year
    
    # Преобразование строк в числа
    left_int = -1
    right_int = -1
    try:
        left_int = int(left)
        right_int = int(right)
    except Exception as e:
        print(e)
        return
    
    # Предварительный ответ
    answer = {'left': left,
              'right': right,
              'raw': raw}

    # Проверяем левую и правую дату на соответствие границам и изменяет ответ
    if not(MIN_YEAR <= left_int <= MAX_YEAR): 
        answer['left'] = ''
    if not(MIN_YEAR <= right_int <= MAX_YEAR):
        answer['right'] = ''
    
    return answer