class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            education_status = 'имеется высшее образование'
        else:
            education_status = 'высшего образования нет'
        print(print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии я {self.occupation}, {education_status}."))

person_a = Person("Ибрахим", "08.08.2006", "программист", True)
person_b = Person("София", "17.03.1999", "дизайнер", False)
person_c = Person("Нурбек", "01.02.1975", "строитель", False)

print(person_a.name, person_a.birth_date, person_a.occupation,person_a.higher_education)
print(person_b.name, person_b.birth_date, person_b.occupation,person_b.higher_education)
print(person_c.name, person_c.birth_date, person_c.occupation,person_c.higher_education)

person_a.introduce()
person_b.introduce()







