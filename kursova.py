from natsort import natsorted


class Contact():
    def __init__(self, phone, name, address):
        self.phone = phone
        self.name = name
        self.address = address

    def contact_add(self, contact_list):
        phone = input("введіть номер телефону: ")
        name = input("введіть ім'я: ")
        address = input("введіть адрес: ")
        contact_list[phone] = {"name": name, "address": address}
        print("контакт додано")

    def delete_contact(self, contact_1):
        nan = input("введіть контакт який хочете видалити: ")
        if nan in contact_1:
            del contact_1[nan]
            print("контакт видалено")
        else:
            print("такого контакту немає виберіть існуючий")
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
        print("-" * 60)
        sorted_by_name = dict(natsorted(self.contact_1.items(), key=lambda x: x[1]["name"]))
        if sorted_by_name:
            for phone, info in sorted_by_name.items():
                print(f"phone: {phone}, name: {info["name"]}, address: {info["address"]}")
        else:
            print("none contact")

class Final(Contact):
    def __init__(self):
        self.contact_1 = {
            "789": {"name": "Ivan Ivanenko", "address": "Kyev"},
            "780": {"name": "Ivan Petrovych", "address": "Franic"},
            "321": {"name": "Petro Petrovych", "address": "Lviv"},
            "555": {"name": "Anna Antonyvna", "address": "Odesa"}
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