def hide_number(account):
    """
    Принимает строку с названием и номером счета, разделяет.
    Возвращает название и последние 4 цифры счета в формате **ХХХХ
    :param account: строка
    :return: "название" + **ХХХХ
    """
    if len(account) > 0:
        number = account.split()
        account_number = ''
        account_name = ''
        for symbol in number:
            if symbol.isdigit():
                account_number += "**" + symbol[-4:]
            else:
                account_name += symbol + ' '
        return account_name + account_number


def hide_card(card):
    """
    Принимает строку с названием и номером карты.
    Возвращает название карты и скрытый номер карты.
    Первый цикл заполняет номер карты символом * с седьмого символа по 12ый,
    и получает имя карты отдельно в список.
    Второй цикл режет скрытый номер по 4 символа и добавляет их в список.
    :param card: строка
    :return: "карта" + ХХХХ ХХ** **** ХХХХ
    """
    split_text = card.split()
    card_name = []
    hide_card = ''
    for num in split_text:
        if num.isdigit():
            hide_card += num[:6] + '*' * len(num[6:12]) + num[-4:]
        else:
            card_name.append(num)

    for i in range(0, len(hide_card), 4):
        card_name.append(hide_card[i:i + 4])

    return ' '.join(card_name)


def check_card_number(account_number):
    """
    Принимает строку с названием счета/карты и номером счета/карты.
    Проверяет длину номера счета/карты. Передает данные в функцию для соответствующего отображения.
    :param account_number: строка
    :return: возвращает скрытый счет
    """
    temp_split = account_number.split()
    for x in temp_split:
        if x.isdigit():
            if len(x) > 16:
                return hide_number(account_number)
            else:
                return hide_card(account_number)
