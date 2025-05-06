from uuid import uuid4

class ValidateBook():
    with open("genders.txt", "r") as arq:
        genders_list = arq.read().split(", ")
    attrs_list = ["title", "author", "year", "gender", "n_pages"]

    def author(self, value):
        author = value.strip()
        while True:
            if author.isalpha(): return gender
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
            if gender in genders_list: return gender
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

class Livro():
    def __init__(self, title, author, year, gender, num_pgs):
        self.id = str(uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.gender = gender
        self.n_pages = n_pages

    def update(self, attr, new_value):
        s_new_value = new_value.strip()

        if attr == "title": 
            setattr(self, attr, s_new_value)
        else:
            vd = getattr(ValidationBook, attr)

            setattr(self, attr, vd(s_new_value))

    
