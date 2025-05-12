import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

from ValidateBook import ValidateBook
import json
from uuid import uuid4

from add_item import addItem
from update_item import updateItem
from show_items import showItems
from delete_item import deleteItem
from filter_items import filterItems

while True:
    vd = ValidateBook()

    print("\n===== CRUD Biblioteca =====\n")
    
    option = input("Escolha uma opção (número):\n -> 1) Adicionar livro\n -> 2) Atualizar livro\n -> 3) Deletar livro\n -> 4) Mostrar livros\n -> 5) Filtrar livros\n -> 6) Sair\n").strip()

    if option in [str(x) for x in range(2, 5)]:
        with open("./data/items.json", "r") as arq:
            try:
                list_items = json.loads(arq.read())["items"]
                if list_items == []:
                    print("\n -> Ainda não há itens na lista!")
                    continue
            except:
                print("\n -> Ainda não há itens na lista!")
                continue

    match option:
        case "1":
            print("\n===== Adicionar livro =====\n")
            
            new_item = {
                "id": str(uuid4()),
                "title": vd.title(input("Insira o título do livro: ")),
                "author": vd.author(input("Insira o autor do livro: ")),
                "year": vd.year(input("Insira o ano do livro: ")),
                "gender": vd.gender(input("Insira o gênero do livro: ")),
                "quantity": vd.quantity(input("Insira a quantidade: "))
            }   

            addItem(new_item)

            print(f"\n -> Livro adicionado!\n  - ID do novo livro: {new_item["id"]}")
        
        
        case "2":
            print("\n===== Atualizar livro =====\n")

            for item in list_items:
                print(f" - Título: {item["title"]} | ID: {item["id"]}")

            id_ = vd.id_(input("\nInsira o ID do item que deseja atualizar: "))
            updateItem(id_)

            print("\n -> Livro atualizado!")
        
        
        case "3":
            print("\n===== Deletar livro =====\n")

            for item in list_items:
                print(f" - Título: {item["title"]} | ID: {item["id"]}")

            id_ = vd.id_(input("\nInsira o ID do item que deseja deletar: "))
            deleteItem(id_)
        
            print("\n -> Livro deletado! ")
        
        case "4":
            print("\n===== Livros da biblioteca =====\n")

            showItems()
            
        case "5":
            print("\n===== Filtrar livros =====\n")

            attrs_arr = []
            values_arr = []

            while True:
                attr = input("Insira o atributo a ser filtrado [T/A/Y/G/Q] (Enter para parar): ")
                if attr == "": break
                attr = vd.attr(attr)
                
                while attr in attrs_arr:
                    attr = vd.attr(input(" -> Atributo já incluído. Tente outro: "))

                if attr == "title":
                    value = input("Insira o valor do atributo: ").strip().title()

                    attrs_arr.append(attr)
                    values_arr.append(value)

                    break
                else:
                    value = eval(f"vd.{attr}(input('Insira o valor do atributo: '))")
    
                attrs_arr.append(attr)
                values_arr.append(value)

                if len(attrs_arr) == 5: break

            filterItems(list(zip(attrs_arr, values_arr)))
        case "6":
            print("\n -> Até mais!")
            break
        
        case _:
            print("\n -> Opção inválida. Programa reiniciando: ")
            continue