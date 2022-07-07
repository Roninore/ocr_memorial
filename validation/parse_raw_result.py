#Files
from validation.names import get_name
from validation.date import get_dates

def parse_raw_result(raw_result = None) -> dict:
    """Приводит значение возвращаемое EasyOCR.readtext() в необходимый вид"""
    try:
        tempStr = max(raw_result,key=len) # Находим нужный абзац c текстом
        
        full_name = get_name(tempStr) # Получаем ФИО
        dates = get_dates(tempStr) # Получаем даты (левую и правую)

        return {'full_name': full_name, # ФИО
                'dates': dates, # Даты
                'raw_result': raw_result} # Изначальная строка (для отладки ошибок или возможности пользователю самому 
                                          # исправить ошибки распознания) 
    except:
        return {'full_name': '', 
                'dates': '', 
                'raw_result': raw_result} 