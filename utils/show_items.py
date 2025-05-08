import json

def showItems():
    with open("./data/items.json", "r") as arq:
        items_list = json.loads(arq.read())["items"]

    for item in items_list:
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

        if not items_list.index(item) == len(items_list) - 1:
            print("\n---------------------------------\n")
     