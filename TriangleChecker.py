class TriangleChecker:
    def __init__(self, a, b, c):
        self.storony = [a, b, c]

    def mozhno_postroit(self):
        if any(side <= 0 for side in self.storony):
            return "С отрицательными числами ничего не выйдет!"
        if not all(isinstance(side, (int, float)) for side in self.storony):
            return "Нужно вводить только числа!"
        a, b, c = sorted(self.storony)
        if a + b > c:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

treugolnik = TriangleChecker(3, 4, 5)
print(treugolnik.mozhno_postroit())
