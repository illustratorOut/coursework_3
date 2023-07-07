from src.utils import load_data_from_json, sort_operations_by_date, sort_the_list_by_date, main

count_last_operations = 5
path_json_file = "src/operations.json"

res_load_json = load_data_from_json(path_json_file)
last_count_date = sort_operations_by_date(res_load_json, count_last_operations)
data_list_sort = sort_the_list_by_date(last_count_date)
main(data_list_sort)
