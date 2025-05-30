import json

class ValidateBook():
    
    def arqs(self):
        with open("./data/genders.json", "r") as arq:
            self.genders_list = json.loads(arq.read())["genders"]
        
        with open("./data/items.json", "r") as arq:
            try:
                self.items_list = json.loads(arq.read())["items"]
            except:
                self.items_list = []
    
    
    def __init__(self):
        self.arqs()
    
    attrs_list = list(zip(["T", "A", "Y", "G", "Q"], ["title", "author", "year", "gender", "quantity"]))
    

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
                    return title.title()
        return title.title()


    def author(self, value):
        author = value.strip()
        
        while True:
            if author.replace(" ", "").isalpha(): return author.title()
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
            if gender.lower() in self.genders_list: return gender.title()
            gender = input(" -> Gênero inválido. Tente novamente: ").strip()
    
    def quantity(self, value):
        try:
            quantity = int(value)
            
            if 0 < quantity:
                 return quantity
            else: 
                raise Exception 
        except:
            while True:
                try:
                    quantity = int(input(" -> Quantidade inválida. Tente novamente: "))
                    if 0 < quantity: return quantity
                except:
                    continue

    def attr(self, value):
        attr = value.strip()


        while True:
            for abrev, longr in self.attrs_list:
                if abrev == attr: return longr
            attr = input(" -> Atributo inválido. Tente novamente: ").strip()

        
