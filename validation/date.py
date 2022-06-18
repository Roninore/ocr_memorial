import re
from datetime import date


def get_dates(raw_string: str=''):
    """Получить отформатированные даты"""
    try:
        answ = re.sub(r'[^0-9.]',' ',raw_string).strip()
        answ = re.sub(r'\s+',' ',answ)

        match = re.match(r'(\d{2}\.\d{2}\.\d{4}).*(\d{2}\.\d{2}\.\d{4})',answ)
        if match:  #Если дата в стандартном виде (dd.mm.yyyy dd.mm.yyyy)
            return {'left': match.group(1),'right': match.group(2),'raw': answ}

        match = re.match(r'.*(\d{2})[0-9\s]+(\d{2}).*(\d{2}).*(\d{2}).*', answ)
        if match: #Если дата в видел yyyy - yyyy
            return validate_date({'left': match.group(1)+match.group(2), 'right': match.group(3)+match.group(4), 'raw': answ})

        
        return {'left': '', 'right': '', 'raw': answ}
    except:
        return {'left': '', 'right': '', 'raw': raw_string}

def validate_date(data):
    """Проверить дату формата yyyy-yyyy"""
    MIN_YEAR = 1500
    MAX_YEAR = date.today().year

    left = -1
    right = -1
    try:
        left = int(data['left'])
        right = int(data['right'])
    except Exception as e:
        print(e)
        return
    
    answer = dict(data)

    if not(MIN_YEAR <= left <= MAX_YEAR):
        answer['left'] = ''
    if not(MIN_YEAR <= right <= MAX_YEAR):
        answer['right'] = ''
    
    return answer