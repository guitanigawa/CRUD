import json

def addItem(new_item):
    with open("./data/items.json", "r") as arq:
        try:
            items_json = json.loads(arq.read())
        except:
            items_json = {"items": []}

    items_list = items_json["items"]
    items_list.append(new_item)
    items_json["items"] = items_list

    with open("./data/items.json", "w") as arq:
        arq.write(json.dumps(items_json))

