class Stack:
    def __init__(self, other=None):
        if other:
            if isinstance(other, self.__calss__):
                self.__book = other.__book[:]
            else:
                raise Exception('Нужен обьект класса'+self.__class.__name__)
        self.__book = list()
    def print(self)->None:
        print('\nСтек книг:',self.__book)

    def push(self, book: str)->None:
        self.__book.append(book)

    def pop(self)->None:
        if len(self.__book):
            self.__book.pop()
        else:
            print('\nСтек книг пуст')

    def find(self,name)->None:
        if len(self.__book):
            arr = list(filter(lambda x: x== name, self.__book))
            print('Ткакая книга есть в списке' if arr else 'Ткакой книги в списке нет')
        else:
            print('\nСтек книг пуст')


if __name__ == '__main__':
    lst = Stack()

    while True:
        print("------------------------------------\n")
        print( "|1 - Добавить книгу               |\n")
        print( "|2 - Удалить книгу                |\n")
        print( "|3 - Вывести на экран             |\n")
        print( "|4 - Поиск книги                  |\n")
        print( "|0 - Выход                        |\n")
        print( "----------------------------------\n")
        cassse = int(input(">>>"))

        if cassse == 1:
            sss = int(input("Введите количество книг коорые хотите ввести:"))
            for i in range(sss):
                name = input("Введите название книги:")
                lst.push(name)

        elif cassse == 2:
            print("Элемент был успешно удалён ;)")
            lst.pop()

        elif cassse ==3:
            lst.print()

        elif cassse == 4:
            cas4 = input("Введите название книги, которую хотите найти:")
            lst.find(cas4)
            print('')
        elif cassse == 0:
            break
        else:
            print("Выберите один из предложенных пунктов меню")

