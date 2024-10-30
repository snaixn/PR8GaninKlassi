class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def get_kg(self):
        return self.__kg

kg = KgToPounds(10)
print(kg.to_pounds())  # 22.05

kg.set_kg(20)
print(kg.to_pounds())  # 44.1

