import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), './'))

import json

class ValidateBook():
    with open("genders.json", "r", encoding="utf-8") as arq:
        genders_list = json.loads(arq.read())["genders"]
    
    with open("items.json", "r") as arq:
        try:
            items_list = json.loads(arq.read())["items"]
        except:
            items_list = {"items": []}
    
    attrs_list = ["T", "A", "Y", "G", "NP"]
    
    def id_(self, value):
        id_ = value.strip()

        ids_list = []
        for item in ValidateBook.items_list:
            if item["id"].casefold() == id_.casefold(): return id_
            ids_list.append(item["id"].casefold())
        
        while not id_ in ids_list:
            id_ = input("ID inválido. Tente novamente: ").strip()

    
    def title(self, value):
        title = value.strip()
    
        for item in ValidateBook.items_list:
            if item["title"].casefold() == title.casefold():
                while item["title"].casefold() == title.casefold():
                    title = input("Título inválido. Tente novamente: ").strip()
                return title

        return title


    def author(self, value):
        author = value.strip()
        while True:
            if author.isalpha(): return author
            author = input("Autor inválido. Tente novamente: ").strip()

    def year(self, value):
        try:
            year = int(value)
            
            if 0 <= year <= 2025:
                 return year
            else: 
                raise Exception 
        except:
            while True:
                try:
                    year = int(input("Ano inválido. Tente novamente: "))
                    if 0 <= year <= 2025: return year
                except:
                    continue 

    def gender(self, value):
        gender = value.strip()
        while True:
            if gender in ValidateBook.genders_list: return gender
            gender = input("Gênero inválido. Tente novamente: ").strip()
    
    def n_pages(self, value):
        try:
            n_pages = int(value)
            
            if 0 < n_pages:
                 return n_pages
            else: 
                raise Exception 
        except:
            while True:
                try:
                    n_pages = int(input("Número inválido. Tente novamente: "))
                    if 0 < n_pages: return n_pages
                except:
                    continue

    def attr(self, value):
        attr = value.strip()
        while True:
            if attr in attrs_list: return attr
            attr = input("Atributo inválido. Tente novamente: ").strip()
    
