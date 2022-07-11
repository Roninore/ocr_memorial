from classes.DateValidator import DateValidator
from classes.FullnameValidator import FullnameValidator

class Validator():
    def __init__(self):
        self.date_validator = DateValidator()
        self.fullname_validator = FullnameValidator()

    def __call__(self, raw_result = None) -> dict:
        return self.parse_raw_result(raw_result)
        
    def parse_raw_result(self,raw_result = None) -> dict:
        """Приводит значение возвращаемое EasyOCR.readtext() в необходимый вид"""
        try:
            tempStr = max(raw_result,key=len) # Находим нужный абзац c текстом
            
            full_name = self.fullname_validator(tempStr) # Получаем ФИО
            dates = self.date_validator(tempStr) # Получаем даты (левую и правую)

            return {'full_name': full_name, # ФИО
                    'dates': dates, # Даты
                    'raw_result': raw_result} # Изначальная строка (для отладки ошибок или возможности пользователю самому 
                                            # исправить ошибки распознания) 
        except Exception as e:
            print('Parse raw resulrt error ->', e)
            return {'full_name': '', 
                    'dates': '', 
                    'raw_result': raw_result} 



