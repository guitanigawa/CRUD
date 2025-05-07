import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from ValidateBook import ValidateBook
import json

vd = ValidateBook()

def updateItem(item_id):
    vd_id = vd.id_(item_id)

    print("\n===== Atualizar Lista! =====\n")

    with open("items.json", "r") as arq:
        try:
            items_json = json.loads(arq.read())
        except:
            print("Ainda não há items na lista!")
            return
        
    items_list = items_json["items"]

    attr_to_change = input("Escolha o atributo a ser alterado [T/A/Y/G/NP]: ")
    while not attr_to_change in ValidateBook.attrs_list:
        attr_to_change = input("Atributo inválido. Tente novamente: ")

    def changeItem(item):
        new_item = item

        if new_item["id"] == vd_id:
            match attr_to_change:
                case "Título":
                    new_item["title"] = input("Insira um novo título: ")
                case "Autor":
                    new_item["author"] = vd.author(input("Insira o novo autor: "))
                case "Ano":
                    new_item["year"] = vd.year(input("Insira um novo ano: "))
                case "Gênero":
                    new_item["gender"] = vd.gender(input("Insira um novo gênero: "))
                case "N Páginas":
                    new_item["n_pages"] = vd.n_pages(input("Insira um novo N de páginas: "))
        
        return new_item

    new_items_list = list(map(changeItem, items_list))
    items_json["items"] = new_items_list
    
    with open("items.json", "w") as arq:
        arq.write(json.dumps(items_json))

    print("\n===== Lista Atualizada! =====\n")
