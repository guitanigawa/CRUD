import json

def filterItems(zip_):
    with open("./data/items.json", "r") as arq:
        items_json = json.loads(arq.read())

    items_list = items_json["items"]

    def filter_func(item):
        match_counter = 0

        for attr, value in zip_:
           if item[attr] == value: match_counter += 1
        
        if len(zip_) == match_counter: return True


    filtered_items = list(filter(filter_func, items_list))

    if filtered_items == []:
        print("\n -> Não há itens correspondentes!")
    else:
        print("\n----- Livros correspondentes -----\n")

        for item in filtered_items:
            print(f" -> ID: {item["id"]}")
            print(f" -> Título: {item["title"]}")
            print(f" -> Autor: {item["author"]}")
            print(f" -> Ano: {item["year"]}")
            print(f" -> Gênero: {item["gender"]}")
            print(f" -> Quantidade: {item["quantity"]}")


            if not filtered_items.index(item) == len(filtered_items) - 1:
                print("\n---------------------------------\n")

    return