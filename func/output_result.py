from datetime import datetime
from func.hide_account import check_card_number


def print_result(last_operation):
    """
    Принимает массив. Цикл запускате поочередный перебор словарей внутри массива,
    Создаются переменные для каждого типа выводимых данных. Проверка на существование
    графы отравителя.
    Переменные "to" "from_" получают данные исходя из проверки внутри функции.
    Печатает полученный результат.
    :param last_operation: массив формата json
    :return: None
    """
    for operation in last_operation:
        the_date = datetime.fromisoformat(operation['date'])
        date_form = the_date.strftime("%H:%M %d.%m.%Y")
        description = operation['description']
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        to = check_card_number(operation['to'])

        if 'from' in operation:
            from_ = check_card_number(operation['from'])
            from_ += ' -> '
        else:
            from_ = ''

        print(
          f"{date_form} {description}\n"
          f'{from_}{to}\n'
          f'{amount} {currency} \n'
              )
