from src.modul import open_json_data, sort_date, main
import pytest

count_last_operations = 5
path_json_file = "./src/operations.json"


def test_open_json_data():
    assert type(open_json_data(path=path_json_file)) == list
    with pytest.raises(TypeError):
        open_json_data()
    with pytest.raises(FileNotFoundError):
        open_json_data("src/ddfssd.py")


def test_sort_date():
    assert type(sort_date(open_json_data(path=path_json_file), count_last_operations)) == tuple
    with pytest.raises(TypeError):
        sort_date()
    assert sort_date([1, 2, 3], count_last_operations) is None


def test_main():
    assert type(main(sort_date(open_json_data(path_json_file), count_last_operations))) == type(None)
    assert main(([1, 2, 3], {1: 1})) is None
