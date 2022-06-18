from validation.names import get_name
from validation.date import get_dates

def parse_raw_result(raw_result = None):
    """Приводит значение возвращаемое EasyOCR.readtext() в необходимый вид"""
    try:
        tempStr = max(raw_result,key=len)
        
        full_name = get_name(tempStr)
        dates = get_dates(tempStr)

        return {'full_name': full_name, 'dates': dates, 'raw_result': raw_result} 
    except:
        return raw_result