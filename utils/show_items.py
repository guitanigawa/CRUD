import json

def showItems():
    with open("./data/items.json", "r") as arq:
        items_list = json.loads(arq.read())["items"]

    for item in items_list:
        print(f" -> ID: {item["id"]}")
        print(f" -> Título: {item["title"]}")
        print(f" -> Autor: {item["author"]}")
        print(f" -> Ano: {item["year"]}")
        print(f" -> Gênero: {item["gender"]}")
        print(f" -> Quantidade: {item["quantity"]}")


        if not items_list.index(item) == len(items_list) - 1:
            print("\n---------------------------------\n")
    
    return