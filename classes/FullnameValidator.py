#Libraries
import json
import difflib
import re
import config

class FullnameValidator():
    def __init__(self) -> None:
        self.names = self.__load_names_from_json() 
        self.surnames = self.__load_surnames_from_json()
        self.partonymics = self.__load_patronymics_from_json()

    def __call__(self,raw_string: str='') -> str:
        return self.get_name(raw_string)

    def __load_names_from_json(self) -> list:
        """Прочитать базу имен из JSON"""
        path_names = config.NAMES_PATH # Путь к базе

        # Вытаскиваем из базы только имена, с количеством любей больше заданного и собираем в список
        MIN_PEOPLE_COUNT = 1000
        names = []
        with open(path_names, encoding='utf-8-sig') as filejson:
            fcc_data = json.load(filejson)
            for i in fcc_data:
                if i['PeoplesCount'] > MIN_PEOPLE_COUNT:
                    names.append(i['Name'])
        
        return names

    def __load_surnames_from_json(self) -> list:
        """Прочитать базу фамилий из JSON"""

        path_surnames = config.SURNAMES_PATH # Путь к базе
        # Вытаскиваем из базы только имена, с количеством любей больше заданного и собираем в список
        surnames = []
        MIN_PEOPLE_COUNT = 1000
        with open(path_surnames, encoding='utf-8-sig') as filejson:
            fcc_data = json.load(filejson)
            for i in fcc_data:
                if i['PeoplesCount'] > MIN_PEOPLE_COUNT:
                    surnames.append(i['Surname'])

        return surnames

    def __load_patronymics_from_json(self) -> list:
        """Прочитать базу отчеств из JSON"""
        partonymics = []
        path_surnames = config.PATRONYMIC_PATH # Путь к базе
        # Вытаскиваем в список все отчества
        with open(path_surnames, encoding='utf-8-sig') as filejson:
            fcc_data = json.load(filejson)
            for i in fcc_data:
                partonymics.append(i)

        return partonymics


    def __validate_name(self,name: str) -> str:
        """Проверка имени"""
        return self.__validate_fullname_part(name,self.names)

    def __validate_surname(self,surname: str) -> str:
        """Проверка фамилии"""
        return self.__validate_fullname_part(surname,self.surnames)

    def __validate_partonymic(self,patronymic: str) -> str:
        """Проверка отчества"""
        return self.__validate_fullname_part(patronymic,self.partonymics)


    def __validate_fullname_part(self, name_part: str, db_list: list) -> str:
        """Общая логика для сравнения части ФИО с базой и поиска похожих.\n 
        '?' - максимально похожее значение. '??' - похожих значений в базе нет """
        try:
            finded_data = difflib.get_close_matches(name_part,db_list)[0] # Берем первое (максимально похожее значение из базы, их может быть больше одного)
            if finded_data == name_part: # При полном совпадении просто возвращаем строку с частью ФИО
                return name_part
            else: # Если найдено похожее, то пишем его в скобках
                return name_part + '(' + finded_data + '?)'
        except: # Не найдено ничего - пишем в скобках ?? (скорее всего распозналось максимально криво)
            return name_part + '(??)'


    def get_name(self,raw_string: str='') -> str:
        """Получить отформатированное ФИО"""
        try:
            answ = re.sub(r'[^А-я\-\s]','',raw_string).strip() # Удаляем лишние символы
            answ = re.sub(r'\s+',' ',answ).split(' ') # Удаляем двойные пробелы и разделяем на массив
            
            filtered = []

            SURNAME_ID = 0
            NAME_ID = 1
            PATRONYMIC_ID = 2                
            MIN_PART_LENGTH = 2

            # Проверяем все слова в массиве, подходящие форматируем и сохраняем
            for str in answ:
                if len(str) > MIN_PART_LENGTH:
                    formated = str[0].upper() + str[1:].lower() # Слово с большой буквы
                    filtered.append(formated)

            # Проводим валидацию каждой части ФИО
            filtered[SURNAME_ID] = self.__validate_surname(filtered[SURNAME_ID])
            filtered[NAME_ID] = self.__validate_name(filtered[NAME_ID])
            filtered[PATRONYMIC_ID] = self.__validate_partonymic(filtered[PATRONYMIC_ID])
            
            answ = ' '.join(filtered) # Через пробел пишем ФИО из масс
            
            return answ
        except Exception as e:
            print('get name error -> ', e)
            return raw_string
