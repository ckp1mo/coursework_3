import pytest
from func.utils import load_operation_json, sort_date
from func.utils import get_5_executed_operations

test_json = r'tests\test_json.json'
date = ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364"]


def test_load_operation_json():
    with pytest.raises(FileNotFoundError):
        assert load_operation_json('')
        assert load_operation_json(test_json) == test_json


def test_sort_date():
    assert sort_date('') == []
    assert sort_date(load_operation_json(test_json)) == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364']
    assert sort_date(['h', 'l', 'y']) == []
    with pytest.raises(TypeError):
        assert sort_date([1, 2, 3])


#
#
def test_get_5_executed_operations():
    assert get_5_executed_operations(load_operation_json(test_json),
                                     sort_date(load_operation_json(test_json))) == load_operation_json(test_json)
    with pytest.raises(AssertionError):
        assert get_5_executed_operations(' ', ' ')
