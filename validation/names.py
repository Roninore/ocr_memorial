import json
import difflib
import re
import config

def load_names():
    """Прочитать базу имен"""
    path_names = config.NAMES_PATH
    names = []
    with open(path_names, encoding='utf-8-sig') as filejson:
        fcc_data = json.load(filejson)
        for i in fcc_data:
            if i['PeoplesCount'] > 1000:
                names.append(i['Name'])
    return names

def load_surnames():
    """Прочитать базу фамилий"""
    surnames = []
    path_surnames = config.SURNAMES_PATH
    with open(path_surnames, encoding='utf-8-sig') as filejson:
        fcc_data = json.load(filejson)
        for i in fcc_data:
            if i['PeoplesCount'] > 1000:
                surnames.append(i['Surname'])
    return surnames

def load_patronymics():
    """Прочитать базу отчеств"""
    partonymics = []
    path_surnames = config.PATRONYMIC_PATH
    with open(path_surnames, encoding='utf-8-sig') as filejson:
        fcc_data = json.load(filejson)
        for i in fcc_data:
            partonymics.append(i)
    return partonymics

names = load_names()
surnames = load_surnames()
partonymics = load_patronymics()

def validate_name(name: str):
    """Проверка имени"""
    try:
        finded_data = difflib.get_close_matches(name,names)[0]
        if finded_data == name:
            return name
        else:
            return name + '(' + finded_data + '?)'
    except:
        return name + '(??)'

def validate_surname(surname: str):
    """Проверка фамилии"""
    try:
        finded_data = difflib.get_close_matches(surname,surnames)[0]
        if finded_data == surname:
            return surname
        else:
            return surname + '(' + finded_data + '?)'
    except:
        return surname + '(??)'

def validate_partonymic(patronymic: str):
    """Проверка отчества"""
    try:
        finded_data = difflib.get_close_matches(patronymic,partonymics)[0]
        if finded_data == patronymic:
            return patronymic
        else:
            return patronymic + '(' + finded_data + '?)'
    except:
        return patronymic + '(??)'

def get_name(raw_string: str=''):
    """Получить отформатированное ФИО"""
    try:
        answ = re.sub(r'[^А-я\-\s]','',raw_string).strip() #
        answ = re.sub(r'\s+',' ',answ).split(' ')
        filtered = []
        for str in answ:
            if len(str) > 2:
                formated = str[0].upper() + str[1:].lower()
                filtered.append(formated)
        filtered[0] = validate_surname(filtered[0])
        filtered[1] = validate_name(filtered[1])
        filtered[2] = validate_partonymic(filtered[2])
        answ = ' '.join(filtered) 
        return answ
    except:
        return raw_string
