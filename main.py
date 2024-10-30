class Soda:
    def __init__(self, dobavka=None):
        self.dobavka = dobavka

    def show_my_drink(self):
        if self.dobavka:
            print(f"Газировка и {self.dobavka}")
        else:
            print("Обычная газировка")

napitok = Soda("лимон")
napitok.show_my_drink()

prostoy_napitok = Soda()
prostoy_napitok.show_my_drink()
