from modul import open_json_data, sort_date, main

count_last_operations = 5
path_json_file = "../src/operations.json"

res_load_json = open_json_data(path_json_file)
last_count_date = sort_date(res_load_json, count_last_operations)
main(last_count_date)
