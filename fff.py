class Human:
    def __init__(self, name, surname, age):
        # self - указатель на объект
        self.name = name
        self.surname = surname
        self.age = age
        self.table = {}

    def get_name(self):
        """Здесь должен быть код, который вернет имя человека"""
        return self.name

    def get_surname(self):
        """Здесь должен быть код, который вернет фамилию человека"""
        return self.surname

    def get_marks(self, subject):
        """Здесь должен быть код, который вернет лист оценок по предмету subject
        из self.table вернуть можно return None"""
        return self.table.get(subject)

    def add_subject(self, subject):
        """Здесь должен быть код, который добавляет в self.table пустой list: []
        на нужный предмет subject"""
        self.table[subject] = []

    def add_mark(self, subject, mark):
        """Здесь должен быть код, который добавляет оценку по предмету subject
        в self.table (Но нужно проверить, есть ли такой предмет,
        если нет, то вывести print('Такого предмета нет'), важно!)"""
        if subject in self.table.keys():
            self.table[subject].append(mark)
        else:
            print('Такого предмета нет')

    def __str__(self):
        """Возврат информации (строка) об этом ученике,
        его Имя, Фамилия, все Оценки"""
        return self.name + "\n" + self.surname + "\n" + str(self.table)


class Dnevnik:
    def __init__(self):
        self.people = set()

    def add(self, human):
        """Здесь должен быть код, который добавит объект человека
        в лист self.people"""
        self.people.add(human)

    def get(self, name, surname, age):
        """Возврат нужного объекта Human (как бы ученика) из self.people по
        его имени, фамилии, возрасту.
        Если нет такого человека, то вернуть None
        """
        for human in self.people:
            if name == human.name and surname == human.surname and age == human.age:
                return human
        return None

    def clear(self):
        """Очистить self.people"""
        self.people.clear()

    def __str__(self):
        """Реализовать возврат информации (строка) о всех учениках"""
        text = ""
        for human in self.people:
            text = text + str(human) + "\n"
        return text


dnevnik = Dnevnik()
human_1 = Human("Alexander", "Starchenko", 19)
human_1.add_subject("Математика")
human_1.add_mark("Математика", 5)
human_1.add_mark("Математика", 5)
human_1.add_mark("Математика", 4)
human_2 = Human("Goida", "ZOV", 22)
human_3 = Human("Git", "Hub", 1337)
human_3.add_subject("ИТ")
human_3.add_mark("ИТ", 5)
human_3.add_mark("ИТ", 5)
human_3.add_mark("Математика", 4) #Должно вывести 'Такого предмета нет'
dnevnik.add(human_1)
dnevnik.add(human_2)
dnevnik.add(human_3)
print(dnevnik)
# Должен вывести что-то по типу (не прям обязательно точь в точь)
# Alexander Starchenko 19 {"Математика": [5, 5, 4]}
# Goida ZOV 22 {}
# Git Hub 1337 {"ИТ": [5, 5]}

some_human = dnevnik.get("Git", "Hub", 1337)
print(some_human.get_name())
#Должно вывести Git

print(some_human.get_marks("ИТ"))
#Должно вывести {"ИТ": [5, 5]}
dnevnik.clear()

print(dnevnik)
# Должно ничего не вывести
# (ну или пустоту, не важно как, главное показать, что ничего нет)
