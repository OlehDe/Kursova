class Contact():
    def __init__(self, phone, name, address):
        self.phone = phone
        self.name = name
        self.address = address

    def contact_add(self, contact_list):
        contact_3 = input("введіть номер телефону, ім'я та адрес щоб добавити контакт в список: ")
        phone, name, address = contact_3.split(", ")
        contact_list[phone] = {"name": name, "address": address}
        print("контакт додано")

    def delete_contact(self, contact_1):
        nan = input("введіть контакт який хочете видалити: ")
        if nan in contact_1:
            del contact_1[nan]
        return

    def print_contact(self, contact_1):
        if contact_1:
            for contacts_1, contacts in contact_1.items():
                print(f"phone: {contacts_1}, name: {contacts["name"]}, address: {contacts["address"]}")
        else:
            print("немає контактів")

    def contact_edit(self, contact_1):
        phone = input("введіть номер який хочере редагувати: ")
        if phone in contact_1:
            new_name = input("введіть нове ім'я: ")
            new_address = input("введіть новий адрес: ")
            contact_1[phone]["name"] = new_name
            contact_1[phone]["address"] = new_address

    def search_contact(self, contact_1):
        sch = input("введіть контакт який ви хочете знайти: ").lower()
        res = {phone: info for phone, info in contact_1.items()
               if sch in phone or sch in info["name"].lower()}
        if res:
            for phone, info in res.items():
                print(f"phone: {phone}, name: {info["name"]}, address: {info["address"]}")
        else:
            print("none contact")

    def sort_contact(self, contact_1):
        sorted_contacts = {kay: contact_1[kay] for kay in sorted(contact_1.keys())}
        if sorted_contacts:
            for phone, info in sorted_contacts.items():
                print(f"phone: {phone}, name: {info["name"]}, address: {info["address"]}")
        else:
            print("none contact")
        # print("-" * 60)
        # def stc(item):
        #     return item[1]["name"]
        # sorted_contacts = sorted(contact_1.items(), key=stc)
        # for phone, info in sorted_contacts:
        #     print(f"phone: {phone}, name: {info["name"]}, address: {info["address"]}")


class Final(Contact):
    def __init__(self):
        self.contact_1 = {
            "789": {"name": "Іван Іваненко", "address": "Київ"},
            "780": {"name": "Іван Петрович", "address": "франік"},
            "321": {"name": "Петро Петрович", "address": "Львів"},
            "555": {"name": "Анна Антонівна", "address": "Одеса"}
        }



    def menu(self):
        while True:
            print("""[1] Додати контакт
[2] Видалити контакт
[3] Переглянути всі контакти
[4] Редагувати контакт
[5] Пошук контакта
[6] Відсортувати контакти
[7] Вийти""")
            namb = input("Виберіть дію: ")

            if namb == "1":
                self.contact_add(self.contact_1)

            elif namb == "2":
                self.delete_contact(self.contact_1)
                print("контакт видалено")

            elif namb == "3":
                self.print_contact(self.contact_1)

            elif namb == "4":
                self.contact_edit(self.contact_1)

            elif namb == "5":
                self.search_contact(self.contact_1)

            elif namb == "6":
                self.sort_contact(self.contact_1)

            elif namb == "7":
                print("програма завершина")
                break

app = Final()
app.menu()

# Final(Contact).final()