from src.Figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        if (a + b) <= c and (a + c)<= b and (b + c) <= a:
            raise ValueError
        self.a = a
        self.b = b
        self.c = c
        per = a + b + c
        p = (a + b + c) / 2
        calc_area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        super().__init__(name= "triangle", area= calc_area, perimeter = per)


