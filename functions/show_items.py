import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from ValidateBook import ValidateBook
import json


def showItems():
    vd = ValidateBook()
    
    with open("items.json", "r") as arq:
        list_items = json.loads(arq.read())["items"]

    
    print("\n===== Itens da Lista =====\n")

    for item in list_items:
        for k, v in item.items():
            match k:
                case "title":
                    print(f" -> Título: {v}")
                case "author":
                    print(f" -> Autor: {v}")
                case "year":
                    print(f" -> Ano: {v}")
                case "gender":
                    print(f" -> Gênero: {v}")
                case "n_pages":
                    print(f" -> N Páginas: {v}")
                case _:
                    print(f" -> {k}: {v}")

        if not list_items.index(item) == len(list_items) - 1:
            print("\n---------------------------------\n")
     