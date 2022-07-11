from classes.DateValidator import DateValidator
from classes.FullnameValidator import FullnameValidator

class Validator():
    def __init__(self):
        self.date_validator = DateValidator()
        self.fullname_validator = FullnameValidator()

    def __call__(self, raw_result:list = None) -> dict:
        return self.parse_raw_result(raw_result)

    def __find_target_strings(self, raw_result:list = None) -> list:
        """Найти строки в которых предположительно может быть ФИО и даты"""
        temp_list = raw_result.copy() # Временная копия массива
        
        MIN_WORDS_IN_STR = 3 # Минимальное число слов в строке (Фамилия Имя Отчество - хотябы 3)
        
        answer = [] # Массив для подходящих строк
        # Находим строки по убыванию длины, с достаточным числом слов
        for i in raw_result:
            longest_str = max(temp_list,key=len)
            if len(longest_str.split()) >= MIN_WORDS_IN_STR:
                answer.append(longest_str)
                temp_list.remove(longest_str)
            else:
                break
        
        return answer

        


    def __parse_one_string(self,raw_string:str = '') -> dict:
        """Получить информацию из строки"""
        try: 
            full_name = self.fullname_validator(raw_string) # Получаем ФИО
            dates = self.date_validator(raw_string) # Получаем даты (левую и правую)

            return {'full_name': full_name, # ФИО
                    'dates': dates, # Даты
                    'raw_string': raw_string} # Изначальная строка (для отладки ошибок или возможности пользователю самому 
                                              # исправить ошибки распознания)
        except Exception as e:
            print('Parse one string error ->', e)
            return {'full_name': '', 
                    'dates': '', 
                    'raw_result': raw_string}


    def parse_raw_result(self,raw_result:list = None) -> list:
        """Приводит значение возвращаемое EasyOCR.readtext() в необходимый вид"""
        try:
            target_strings = self.__find_target_strings(raw_result) # Строки в которых могут быть данные
            
            answer = [] # Найденные данные
            # Ищем ФИО и даты в каждой из строк
            for string in target_strings:
                temp_info = self.__parse_one_string(string)
                if temp_info:
                    answer.append(temp_info)
            
            return answer

            
        except Exception as e:
            print('Parse raw result error ->', e)
            return []



