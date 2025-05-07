import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), './'))

import json

class ValidateBook():
    
    
    def arqs(self):
        with open("genders.json", "r", encoding="utf-8") as arq:
            self.genders_list = json.loads(arq.read())["genders"]
        
        with open("items.json", "r") as arq:
            try:
                self.items_list = json.loads(arq.read())["items"]
            except:
                self.items_list = []
    
    
    def __init__(self):
        self.arqs()
    
    
    attrs_vd = ["T", "A", "Y", "G", "NP"]
    
    
    
    def id_(self, value):
        id_ = value.strip()

        ids_list = []

        for item in self.items_list:
            if item["id"] == id_: return id_
            ids_list.append(item["id"])

        while not id_ in ids_list:
            id_ = input(" -> ID inválido. Tente novamente: ").strip()

    
    def title(self, value):
        title = value.strip()

        if self.items_list != []:
            for item in self.items_list:
                if item["title"].casefold() == title.casefold() or title == "":
                    while item["title"].casefold() == title.casefold() or title == "":
                        title = input(" -> Título inválido. Tente novamente: ").strip()
                    return title.capitalize()
        return title.capitalize()


    def author(self, value):
        author = value.strip()
        while True:
            if author.isalpha(): return author.capitalize()
            author = input(" -> Autor inválido. Tente novamente: ").strip()

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
                    year = int(input(" -> Ano inválido. Tente novamente: "))
                    if 0 <= year <= 2025: return year
                except:
                    continue 

    def gender(self, value):
        gender = value.strip()
        while True:
            if gender.lower() in self.genders_list: return gender.capitalize()
            gender = input(" -> Gênero inválido. Tente novamente: ").strip()
    
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
                    n_pages = int(input(" -> Número inválido. Tente novamente: "))
                    if 0 < n_pages: return n_pages
                except:
                    continue

    def attr(self, value):
        attr = value.strip()
        while True:
            if attr in self.attrs_vd: return attr
            attr = input(" -> Atributo inválido. Tente novamente: ").strip()
    
