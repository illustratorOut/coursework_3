from src.utils import load_data_from_json, sort_operations_by_date, main, sort_the_list_by_date
import pytest

count_last_operations = 5
path_json_file = "./src/operations.json"
result = sort_operations_by_date(load_data_from_json(path=path_json_file), count_last_operations)


def test_open_json_data():
    assert type(load_data_from_json(path=path_json_file)) == list
    with pytest.raises(TypeError):
        load_data_from_json()
    with pytest.raises(FileNotFoundError):
        load_data_from_json("src/ddfssd.py")


def test_sort_date():
    assert type(sort_operations_by_date(load_data_from_json(path=path_json_file), count_last_operations)) == tuple
    with pytest.raises(TypeError):
        sort_operations_by_date()
    assert sort_operations_by_date([1, 2, 3], count_last_operations) is None


def test_sort_operations_by_date():
    assert type(sort_the_list_by_date(result)) == type({})


def test_main():
    assert type(main(sort_the_list_by_date(result))) == type(None)
