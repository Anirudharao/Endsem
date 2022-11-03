class Person:
    count = 0
    l = []
    def __init__(self, name, age):
        self.name1 = name
        self.age1 = age
        Person.count += 1
        ele = [name, age]
        Person.l.append(ele)

        def changeAge(self):
            self.age1 = 69

    def display(self):
        # print("Name: ", self.name1)
        # print("Age: ", self.age1)
        print(Person.l)


p1 = Person("Dhoni", 42)
p2 = Person("Kohli", 35)

p1.display()

print(Person.count)