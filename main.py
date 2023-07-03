import json
from datetime import datetime, date

last_operations = 5
"""
Последние 5 выполненных (EXECUTED) операций выведены на экран.
"""
"""
Операции разделены пустой строкой.
"""
"""
Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
"""
"""
Сверху списка находятся самые последние операции (по дате).
"""
"""
Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX 
(видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
"""
"""
Номер счета замаскирован и не отображается целиком в формате  **XXXX 
(видны только последние 4 цифры номера счета).
"""


def open_json_data(path: str) -> list:
    """Чтение json файла -> return list"""
    with open(path, mode="r", encoding="utf-8") as file:
        return json.load(file)


def sort_date(value: list, last_operations: int):
    sorted_date = {}
    for i in value:
        try:
            if i["state"] == "EXECUTED":
                sorted_date[i["date"]] = i
                if len(sorted_date) == last_operations:
                    return sorted(sorted_date, reverse=True)[:5], sorted_date
        except:
            pass


def main(value):
    a = value[0]
    b = value[1]

    for i in a:
        res_data = str(b[i]["date"]).split("T")[0].split("-")
        res_description = b[i]["description"]
        print(".".join(res_data[::-1]), res_description)
        try:
            res_from = b[i]["from"]
        except:
            res_from = None
        try:
            res_to = b[i]["to"]
        except:
            res_to = None
        print(res_from, "->", res_to)
        print("\n")


result = open_json_data("operations.json")
last_5_date = sort_date(result, last_operations)

main(last_5_date)
