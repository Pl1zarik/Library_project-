class Book():
    def __init__(self, title, author, year):
        # self.title = title
        self.author = author
        self.year = year
    
    # def info(self):
    #     print'Название:', title,'Автор:', author,'Год', year)

class fuction_library():
    def __init__(self):
        self.library = {}
    
    def add_book(self, title, author, year):
        if title in library:
            print('Книга уже есть')
        else:
            self.library[title] = Book(author, year)
            # self.library.append(new_book)
            print('Новая книга', title ,'была добавлена')
        return
    
    def remove_book(self, titel):   
        if titel in self.library:
            del self.library[titel]
        else:
            print('Данная книга не найдена в библиотеке')
        return
    
    def find_book(self, titel):
        if titel in self.library:
            print(self.library[titel])
        else:
            print('Данная книга не найдена в библиотеке')
        return
    
    def show_books(self):
        if len(self.library) == 0:
            print('Книг пока нет')
        else:
            print(self.library)
        return
def Help():
    print(
        'Добавить книгу\nУдалить книгу\nНайти книгу\nПоказать все книги'
    )
book = input('Введите запрос (Help - все комманды):').lower()
while book != 'стоп':
    if book == 'Добавить книгу':
        titel = input('Введите название').title()
        author = input('Введите автора').title()
        year = input('Введите год написания')
        fuction_library.add_book(title, author, year)
        


        



        
    
