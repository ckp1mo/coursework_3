import json


def load_operation_json(operations):
    """
    Принимает файл json, загружает его.
    :param operations: json массив
    :return: массив
    """
    with open(operations, 'r', encoding="utf-8") as file:
        file = json.load(file)
        return file


def sort_date(json_dict):
    """
    Принимает массив данных, создает список с отсортированными датами в обратном порядке.
    :param json_dict: массив json
    :return: список дат reverse=True
    """
    sort_date_list = sorted([d['date'] for d in json_dict if 'date' in d], reverse=True)
    return sort_date_list


def get_5_executed_operations(operations, sort_date_list):
    """
    Принимает массив json, список дат.
    Сопоставляет дату из списка с датой из json, проверяет состояние операции на "EXECUTED",
    Добавляет в список полную операцию из массива.
    :param operations: массив json
    :param sort_date_list: список
    :return: список
    """
    five_operations = []
    for i in sort_date_list:
        if len(five_operations) == 5:
            break
        for x in operations:
            if 'state' in x:
                if x['state'] == 'EXECUTED':
                    if i == x['date']:
                        five_operations.append(x)
    return five_operations
