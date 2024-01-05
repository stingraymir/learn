class Animal():

    def __init__(self, age) -> None:
        self.age = age
        self.name = None

    def get_age(self):
        return self.age
    

cat = Animal(1.5)
