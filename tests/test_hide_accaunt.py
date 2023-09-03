from utils.hide_account import hide_number, hide_card, check_card_number


def test_hide_number():
    assert hide_number('') == None
    assert hide_number('account 3311009434') == 'account **9434'
    assert hide_number('account') == 'account '


def test_hide_card():
    assert hide_card('') == ''
    assert hide_card('Visa Classic') == 'Visa Classic'
    assert hide_card('44126599') == '4412 65** 6599'


def test_check_card_number():
    assert check_card_number('account 44125555666699991111') == 'account **1111'
    assert check_card_number('Visa Classic 4289645133554978') == 'Visa Classic 4289 64** **** 4978'
    assert check_card_number(' ') == None