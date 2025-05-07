import json

def deleteItem(item_id):
    with open("../items.json", "r") as arq:
        