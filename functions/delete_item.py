import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from ValidateBook import ValidateBook
import json

def deleteItem(item_id):
    vd = ValidateBook()
    vd_id = vd.id_(item_id)

    with open("items.json", "r") as arq:
        items_json = json.loads(arq.read())
    
    items_list = items_json["items"]
        
    for item in items_list:
        if item["id"] == vd_id: items_list.remove(item)

    items_json["items"] = items_list

    with open("items.json", "w") as arq:
        arq.write(json.dumps(items_json))

    print("\n -> Item deletado! ")