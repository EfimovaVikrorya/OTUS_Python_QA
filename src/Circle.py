from src.Figure import Figure
import  math

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        calc_area = math.pi * radius
        calc_per = 2 * math.pi * radius
        super().__init__(name="rectangle", area=calc_area, perimeter=calc_per)
