class Animal():

    def __init__(self, age) -> None:
        self.age = age
        self.name = None

    def get_age(self):
        return self.age
    
    def set_age(self, years):
        self.age = years

    def set_name(self, name):
        self.name = name 

    def get_name(self):
        return self.name
    
    def __str__(self):
        return "animal: " + str(self.name)+":" + str(self.age)


class Cat(Animal):
    def speak(self):
        return ("Meoww")
    def __str__(self):
        return (f"Cat named {self.name} is {self.age} years old")


my_cat = Cat(1)
my_cat.set_name ("Gandalf")
my_cat.set_age(1.5)

print(my_cat)
print(my_cat.get_name())
