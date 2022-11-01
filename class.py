class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def greet(self):
        print(f"Hello my name is {self.name}")


class Student(Person):
    def __init__(self, name, age, entrance_year, subject):
        super().__init__(name, age)
        self.entrance_year = entrance_year
        self.subject = subject

    def __str__(self):
        return f"I'm a student with the name {self.name} and age {self.age}. I joined at {self.entrance_year}."

    def what_the_subject(self):
        print(f"I'm studying \"{self.subject}\"")


p1 = Person("Hasan", 17)
print(p1)
p1.greet()

s1 = Student("Jack", 29, 2022, "Computer Science")
print(s1)
s1.what_the_subject()
