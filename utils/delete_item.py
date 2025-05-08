import json

def deleteItem(item_id):
    with open("./data/items.json", "r") as arq:
        items_json = json.loads(arq.read())

    
    items_list = items_json["items"]
        
    for item in items_list:
        if item["id"] == item_id: items_list.remove(item)

    items_json["items"] = items_list

    with open("./data/items.json", "w") as arq:
        arq.write(json.dumps(items_json))
