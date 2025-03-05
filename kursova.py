def contact(contact_1, name, phone, address):
    contact_1[name] = {"phone": phone, "address": address}
    return contact_1

def menu():
    print("""
   [1] Додати контакт
   [2] Видалити контакт
   [3] Переглянути всі контакти
   [4] Вийти""")

def minus(contact_1):
    nan = input("введіть контакт який хочете видалити: ")
    if nan in contact_1:
        del contact_1[nan]
    return



def final():
    contact_1 = {}
    while True:
        menu()
        namb = input("введіти операцію: ")

        if namb == "1":
            contact_3 = input("введіть ім'я, номер телефону та адрес щоб добавити контакт в список: ")
            name, phone, address = contact_3.split(", ")
            contact_1 = contact(contact_1, name, phone, address)
            print("контакт додано")

        elif namb == "2":
            contact_1 = minus(contact_1)
            print("контакт видалено")

        elif namb == "3":
            print("Список контактів:", contact_1)

        elif namb == "4":
            print("програма завершина")
            break


final()