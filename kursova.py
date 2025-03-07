def contact(contact_1, phone, name, address):
    contact_1[phone] = {"name": name, "address": address}
    return contact_1

def menu():
    print("""
   [1] Додати контакт
   [2] Видалити контакт
   [3] Переглянути всі контакти
   [4] Редагувати контакт
   [5] Пошук контакта
   [6] Вийти""")

def contact_all(contact_list):
    contact_3 = input("введіть номер телефону, ім'я та адрес щоб добавити контакт в список: ")
    phone, name, address = contact_3.split(", ")
    contact_list[phone] = {"name": name, "address": address}
    print("контакт додано")

def minus(contact_1):
    nan = input("введіть контакт який хочете видалити: ")
    if nan in contact_1:
        del contact_1[nan]
    return

def new_contact(contact_1):
    phone = input("введіть номер який хочере редагувати: ")
    if phone in contact_1:
        new_name = input("введіть нове ім'я: ")
        new_address = input("введіть новий адрес: ")
        contact_1[phone]["name"] = new_name
        contact_1[phone]["address"] = new_address

def search_contact(contact_1):
    sch = input("введіть контакт який ви хочете знайти: ")
    sch = sch.lower()
    if sch in contact_1:
        print(f'phone: {sch} name: {contact_1[sch]["name"]}, address: {contact_1[sch]["address"]}')


def final():
    contact_1 = {
    "789": {"name": "Іван Іваненко", "address": "Київ"},
    "321": {"name": "Петро Петрович", "address": "Львів"},
    "555": {"name": "Анна Антонівна", "address": "Одеса"}
}


    while True:
        menu()
        namb = input("введіти операцію: ")

        if namb == "1":
            contact_all(contact_1)


        elif namb == "2":
            minus(contact_1)
            print("контакт видалено")

        elif namb == "3":
            if contact_1:
                for phone, info in contact_1.items():
                    print(f'phone: {phone} name: {info["name"]}, address: {info["address"]}')
            else:
                print("немає контактів")

        elif namb == "4":
            new_contact(contact_1)

        elif namb == "5":
            search_contact(contact_1)


        elif namb == "6":
            print("програма завершина")
            break


final()