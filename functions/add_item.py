import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from uuid import uuid4
from ValidateBook import ValidateBook
import json


def addItem():
    vd = ValidateBook()
    
    print("\n===== Adicionar livro =====\n")

    new_item = {
        "id": str(uuid4()),
        "title": vd.title(input("Insira o título do livro: ")),
        "author": vd.author(input("Insira o autor do livro: ")),
        "year": vd.year(input("Insira o ano do livro: ")),
        "gender": vd.gender(input("Insira o gênero do livro: ")),
        "n_pages": vd.n_pages(input("Insira o número de páginas: "))
    }


    with open("items.json", "r", encoding="utf-8") as arq:
        try:
            items_json = json.loads(arq.read())
        except:
            items_json = {"items": []}
        items_list = items_json["items"]
    
    items_list.append(new_item)
    items_json["items"] = items_list

    with open("items.json", "w") as arq:
        arq.write(json.dumps(items_json))
    
    print(f"\n -> Livro adicionado!\n  - ID do novo livro: {new_item["id"]}")
