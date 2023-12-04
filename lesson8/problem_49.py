# Задача №49. Решение в группах
# Создать телефонный справочник с  возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер  телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
#    записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 60 минут


def read_data(filename):
    with open(filename, "r") as book:
        return [lines.rstrip().split(",") for lines in book]


def write_data(filename, phone_book):
    with open(filename, "w") as book:
        phone_book_str = ""
        for line in phone_book:
            phone_book_str = phone_book_str + ",".join(line) + "\n"
        book.write(phone_book_str)
    print("\n---SAVED----\n")
    time.sleep(2)
    return


def show_all(phone_book):
    for i in phone_book:
        [print(j, end="\t\t") for j in i]
        print()


def edit(item):
    print("Old Data: ", item)
    for i in range(1, len(item)):
        print("Old Data: ", item[i])
        item_tmp = input("Enter New Data: ")
        if item_tmp:
            item[i] = item_tmp
    return item


def find_data(phone_book):
    x = input("What are you looking for? ").title()
    for i in range(len(phone_book)):
        if x in phone_book[i]:
            return i
    return -1


def make_new_person(phone_book):
    new_person = [str(int(phone_book[-1][0]) + 1)]
    for i in range(len(phone_book[0]) - 1):
        new_person.append(input(f"Enter the {i + 1} field of the directory: "))
    new_person[-1] += "\n"
    return new_person


import time

PHONEBOOK = 'phonebook.txt'
phonebook = read_data(PHONEBOOK)
game = True

while game:
    print("\tEnter [1] for list all\t\tEnter [9] to save changes\n"
          "\tEnter [2] for search\t\tEnter [0] for quit\n",
          "\tEnter [3] for add person\n")
    command = input().lower()
    if command == "1":
        show_all(phonebook)
    elif command == "2":
        answ_item = find_data(phonebook)
        if answ_item != -1:
            print(phonebook[answ_item], "\n")
            answ = input("Edit? [e]  Delete? [d]  Skip? [s]").lower()
            if answ == "e":
                phonebook[answ_item] = edit(phonebook[answ_item])
                write_data(PHONEBOOK, phonebook)
            elif answ == "d":
                phonebook.pop(answ_item)
                for i in range(len(phonebook)-1):
                    phonebook[i][0] = str(i+1)
                write_data(PHONEBOOK, phonebook)
        else:
            print("Don`t find\n")
    elif command == "3":
        phonebook.append(make_new_person(phonebook))
        if input("Save changes to a file? [y/n]") == "y":
            write_data(PHONEBOOK, phonebook)
    elif command == "9":
        write_data(PHONEBOOK, phonebook)
    elif command == "0":
        print("Game over")
        game = False
    else:
        print("Your entered the wrong character")
