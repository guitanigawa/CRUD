import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'functions'))

from add_item import addItem
from update_item import updateItem
import json


while True:
    print("===== CRUD Biblioteca =====\n")
    
    option = input("Escolha uma opção:\n -> 1) Adicionar item\n -> 2) Atualizar item\n -> 3) Sair\n")

    match option:
        case "1":
            addItem()
        case "2":
            id_ = input("Insira o ID do item que deseja atualizar: ")

            updateItem(id_)
        case "3":
            break
        case _:
            print("Opção inválida. Programa reiniciando: ")
            continue