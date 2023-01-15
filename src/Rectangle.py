from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__(name= "rectangle", area= width * height , perimeter = width + height)
