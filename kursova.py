class Contact():
    def __init__(self, phone, name, address, data, contact_1, add_date):
        self.add_date = add_date
        self.contact_1 = contact_1
        self.phone = phone
        self.name = name
        self.address = address
        self.data = data

    def contact_add(self, contact_list, data_add):
        phone = input("Введіть номер телефону: ")
        if phone in contact_list:
            print("Цей номер вже є в телефонні книзі")
            return
        if not phone.isdigit(): # isdigit це короче якщо хоча б один символ не є цифрою буде False, а якщо всі цифри, то буде True
            print("Номер має бути цифрами")
            return
        name = input("Введіть ім'я: ")
        address = input("Введіть адрес: ")
        data = input("Введіть дату в форматі(РРРР-ММ-ДД): ")
        contact_list[phone] = {"name": name, "address": address}
        print("Контакт додано")
        data_add[phone] = data

    def delete_contact(self, contact_1):
        nan = input("Введіть номер контакту який хочете видалити: ")
        if nan in contact_1:
            del contact_1[nan]
            print("Контакт видалено")
        else:
            print("Такого контакту немає виберіть існуючий")
        return

    def print_contact(self, contact_1, add_data):
        for contacts_1, contacts in contact_1.items():
            print(f"phone: {contacts_1}, name: {contacts["name"]}, address: {contacts["address"]}, data: {add_data[contacts_1]}")

    def contact_edit(self, contact_1):
        phone = input("Введіть номер контакту який хочете редагувати: ")
        if phone in contact_1:
            new_name = input("Введіть нове ім'я: ")
            new_address = input("Введіть новий адрес: ")
            contact_1[phone]["name"] = new_name
            contact_1[phone]["address"] = new_address
        else:
            print("Такого контакту немає виберіть існуючий")

    def search_contact(self, contact_1, add_data):
        sch = input("Введіть (номер або назву) контакту який ви хочете знайти: ").lower()
        res = {phone: info for phone, info in contact_1.items()
               if sch in phone or sch in info["name"].lower()}
        for phone, info in res.items():
            print(f"phone: {phone}, name: {info["name"]}, address: {info["address"]}, data: {add_data[phone]}")


    def sorted_1(self, contact_1, add_data):
        sorted_by_phone = {kay: contact_1[kay] for kay in sorted(contact_1.keys())}
        for phone, info in sorted_by_phone.items():
            print(f"phone: {phone}, name: {info["name"]}, address: {info["address"]}, data: {add_data[phone]}")


    def sorted_2(self, add_data):
        sorted_by_name = dict(sorted(self.contact_1.items(), key=lambda x: x[1]["name"]))

        for phone, info in sorted_by_name.items():
            print(f"phone: {phone}, name: {info["name"]}, address: {info["address"]}, data: {add_data[phone]}")


    def sorted_3(self, contact_1,):
        sorted_by_date = {phone: contact_1[phone] for phone in sorted(contact_1, key=lambda x: self.add_date[x])}

        for phone, info in sorted_by_date.items():
            print(f"phone: {phone}, name: {info['name']}, address: {info['address']}, date: {self.add_date[phone]}")


class Final(Contact):
    def __init__(self):
        self.contact_1 = {
            "380123456789": {"name": "Ivan Ivanenko", "address": "Kyev"},
            "380923456780": {"name": "Ivan Petrovych", "address": "Franic"},
            "380987654321": {"name": "Petro Petrovych", "address": "Lviv"},
            "380555555555": {"name": "Anna Antonyvna", "address": "Odesa"}
        }
        self.add_date = {
            "380123456789": "2025-04-01",
            "380923456780": "2025-04-02",
            "380987654321": "2025-03-30",
            "380555555555": "2025-03-29"
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
            dia = ("""[1] Сортувати за номером телефону
[2] Сортувати за імям
[3] Сортувати за датою створення""")
            namb = input("Виберіть дію: ")

            if namb == "1":
                self.contact_add(self.contact_1, self.add_date)

            elif namb == "2":
                self.delete_contact(self.contact_1)

            elif namb == "3":
                self.print_contact(self.contact_1, self.add_date)

            elif namb == "4":
                self.contact_edit(self.contact_1)

            elif namb == "5":
                self.search_contact(self.contact_1, self.add_date)

            elif namb == "6":
                print(dia)
                nams = input("Виберіть дію: ")
                if nams == "1":
                    self.sorted_1(self.contact_1, self.add_date)
                elif nams == "2":
                    self.sorted_2(self.contact_1, self.add_date)
                elif nams == "3":
                    self.sorted_3(self.contact_1, self.add_date)
                else:
                    print("такої дії не існує")


            elif namb == "7":
                print("програма завершина")
                break

app = Final()
app.menu()

# Final(Contact).final()