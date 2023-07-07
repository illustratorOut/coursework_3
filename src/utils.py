import json
from datetime import datetime, date


def load_data_from_json(path: str) -> list:
    with open(path, mode="r", encoding="utf-8") as file:
        return json.load(file)


def sort_operations_by_date(value: list, last_operations: int):
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


def sort_the_list_by_date(list):
    a = list[0]
    b = list[1]
    new_list_sort_date = {date.fromisoformat(i.split("T")[0]).strftime("%d.%m.%Y"): b[i] for i in a}
    return new_list_sort_date


def main(value):
    """Преобразования в нужный формат и вывод на экран"""
    text_else = " "
    for k, v in value.items():
        if k:
            print(k, end=' ')
        else:
            print(text_else)
        if v["description"]:
            res_description = v["description"]
            print(res_description)
        else:
            print(text_else)
        if v.get("from", None):
            res = v["from"].split()[-1]
            x = res[:6] + (len(res) - 10) * '*' + res[-4:]
            card_number = [x[v:v + 4] for v in range(0, len(x), 4)]
            res_from = " ".join(card_number)
            print(res_from, "->", end=' ')
        else:
            print(text_else, "->", end=' ')
        if v.get("to", None):
            res_to = v["to"]
            res_to = (len(list(res_to.split()[-1:][0])) - 4) * '*' + res_to[-4::]
            print(res_to)
        else:
            print(text_else)
        if v.get("operationAmount", None)["amount"]:
            res_amount = v["operationAmount"]["amount"]
            print(res_amount, end=' ')
        else:
            print(text_else, end=' ')
        if v.get("operationAmount", None)["currency"]["name"]:
            res_name = v["operationAmount"]["currency"]["name"]
            print(res_name, "\n")
        else:
            print(text_else, "\n")
