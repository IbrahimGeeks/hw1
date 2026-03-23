class Person:
    def __init__(self, name, birth_date, profession):
        self.name = name
        self.birth_date = birth_date
        self.profession = profession

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, работаю {self.profession}")


class Friend(Person):
    def __init__(self, name, birth_date, profession, hobby, owner):
        super().__init__(name, birth_date, profession)
        self.hobby = hobby
        self.owner = owner

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг {self.owner}, я родился {self.birth_date}, работаю {self.profession}")


class Classmate(Person):
    def __init__(self, name, birth_date, profession, group_name, owner):
        super().__init__(name, birth_date, profession)
        self.group_name = group_name
        self.owner = owner

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник {self.owner}, я родился {self.birth_date}, работаю {self.profession}")


friend1 = Friend("Артём", "12.05.2000", "разработчик", "футбол", "Данияра")
friend2 = Friend("Илья", "03.11.2001", "дизайнер", "музыка", "Данияра")

classmate1 = Classmate("Максим", "25.07.2000", "программист", "10-Б", "Данияра")
classmate2 = Classmate("Кирилл", "14.02.2001", "инженер", "10-Б", "Данияра")

friend1.introduce()
friend2.introduce()
classmate1.introduce()
classmate2.introduce()