class Nikolay:
    def __init__(self, name, age):
        if name.lower() == "николай":
            self.name = name
        else:
            self.name = "Я не " + name + ", а Николай"
        self.age = age

    def __setattr__(self, key, value):
        if key in ["name", "age"]:
            super().__setattr__(key, value)
        else:
            raise AttributeError("Нельзя добавлять новые атрибуты!")

person = Nikolay("Максим", 25)
print(person.name)  # Я не Максим, а Николай
