import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))

from add_item import addItem
from update_item import updateItem
from show_items import showItems
from delete_item import deleteItem
import json

while True:
    print("\n===== CRUD Biblioteca =====\n")
    
    option = input("Escolha uma opção (número):\n -> 1) Adicionar livro\n -> 2) Atualizar livro\n -> 3) Mostrar livro\n -> 4) Deletar livro\n -> 5) Sair\n").strip()

    match option:
        case "1":
            addItem()
        
        case "2":
            
            with open("items.json", "r") as arq:
                try:
                    list_items = json.loads(arq.read())["items"]
                    if list_items == []:
                        print("\n -> Ainda não há itens na lista!")
                        continue
                except:
                    print("\n -> Ainda não há itens na lista!")
                    continue

            print("\n===== Atualizar livro =====\n")

            for item in list_items:
                print(f" - Título: {item["title"]} | ID: {item["id"]}")

            id_ = input("\nInsira o ID do item que deseja atualizar: ")

            updateItem(id_)
        
        case "3":
            showItems()
        
        case "4":
            with open("items.json", "r") as arq:
                try:
                    list_items = json.loads(arq.read())["items"]
                    if list_items == []:
                        print("\n -> Ainda não há itens na lista!")
                        continue
                except:
                    print("\n -> Ainda não há itens na lista!")
                    continue

            print("\n===== Deletar livro =====\n")

            for item in list_items:
                print(f" - Título: {item["title"]} | ID: {item["id"]}")

            id_ = input("\nInsira o ID do item que deseja deletar: ")

            deleteItem(id_)
        case "5":
            print(" -> Até mais!")
            break
        case _:
            print("\n -> Opção inválida. Programa reiniciando: ")
            continue