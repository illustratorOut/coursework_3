import json
from datetime import datetime, date


def open_json_data(path: str) -> list:
    """Чтение json файла -> return list"""
    with open(path, mode="r", encoding="utf-8") as file:
        return json.load(file)


def sort_date(value: list, last_operations: int):
    """Сортирует по дате последние 'last_operations' - кол-во выполненных операций"""
    sorted_date = {}
    for i in value:
        try:
            if i["state"] == "EXECUTED":
                sorted_date[i["date"]] = i
                if len(sorted_date) == last_operations:
                    return sorted(sorted_date, reverse=True)[:last_operations], sorted_date
        except:
            pass


def main(value):
    """Преобразования в нужный формат и вывод на экран"""
    a = value[0]
    b = value[1]

    for i in a:
        try:
            res_data = str(b[i]["date"]).split("T")[0]
            thedate = date.fromisoformat(res_data).strftime("%d.%m.%Y")
        except:
            res_data = None
            thedate = None
        try:
            res_description = b[i]["description"]
        except:
            res_description = None
        try:
            res = b[i]["from"].split()[-1]
            x = res[:6] + (len(res) - 10) * '*' + res[-4:]
            card_number = [x[i:i + 4] for i in range(0, len(x), 4)]
            res_from = " ".join(card_number)

        except:
            res_from = None
        try:
            res_to = b[i]["to"]
            res_to = (len(list(res_to.split()[-1:][0])) - 4) * '*' + res_to[-4::]
        except:
            res_to = None
        try:
            res_amount = b[i]["operationAmount"]["amount"]
        except:
            res_amount = None
        try:
            res_name = b[i]["operationAmount"]["currency"]["name"]
        except:
            res_name = None

        print(thedate, res_description)
        print(res_from, "->", res_to)
        print(res_amount, res_name, "\n")
