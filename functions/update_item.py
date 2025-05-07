import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from ValidateBook import ValidateBook
import json


def updateItem(item_id):
    vd = ValidateBook()
    vd_id = vd.id_(item_id)

    with open("items.json", "r") as arq:
        try:
            items_json = json.loads(arq.read())
        except:
            print("\n -> Ainda não há items na lista!")
            return

    

    items_list = items_json["items"]

    attr_to_change = vd.attr(input("Escolha o atributo a ser alterado [T/A/Y/G/NP]: "))

    def changeItem(item):
        new_item = item

        if new_item["id"] == vd_id:
            match attr_to_change:
                case "T":
                    new_item["title"] = input(f"Insira um novo título [Antigo: {item["title"]}]: ")
                case "A":
                    new_item["author"] = vd.author(input(f"Insira o novo autor [Antigo: {item["author"]}]: "))
                case "Y":
                    new_item["year"] = vd.year(input(f"Insira um novo ano [Antigo: {item["year"]}]: "))
                case "G":
                    new_item["gender"] = vd.gender(input(f"Insira um novo gênero [Antigo: {item["gender"]}]: "))
                case "NP":
                    new_item["n_pages"] = vd.n_pages(input(f"Insira um novo N de páginas [Antigo: {item["n_pages"]}]: "))
        
        return new_item

    new_items_list = list(map(changeItem, items_list))
    items_json["items"] = new_items_list
    
    with open("items.json", "w") as arq:
        arq.write(json.dumps(items_json))

    print("\n -> Item atualizado!")
