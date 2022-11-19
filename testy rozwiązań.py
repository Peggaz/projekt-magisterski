


class student:

    def __init__(self, name, surname, age, value):
        self.name = name
        self.surname = surname
        self.age = age
        self.values = values

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.values}"

    def __repr__(self):
        return f"{self.name} {self.surname} {self.age} {self.values}"

