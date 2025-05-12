import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "models"))

from ValidateBook import ValidateBook
import json

def updateItem(item_id):
    vd = ValidateBook()

    with open("./data/items.json", "r") as arq:
        items_json = json.loads(arq.read())


    items_list = items_json["items"]
    
    attr_to_change = vd.attr(input("Escolha o atributo a ser alterado [T/A/Y/G/Q]: "))

    def changeItem(item):
        new_item = item

        if new_item["id"] == item_id:
            new_item[attr_to_change] = eval(f"""vd.{attr_to_change}(input(f'Insira o novo valor do atributo [Antigo: "{item[attr_to_change]}"']: ))""")

        return new_item

    new_items_list = list(map(changeItem, items_list))
    items_json["items"] = new_items_list
    
    with open("./data/items.json", "w") as arq:
        arq.write(json.dumps(items_json))

    return

