from src.Figure import Figure

class Square(Figure):
    def __init__(self, width):
        self.width = width
        super().__init__(name= "rectangle", area= width * width , perimeter = width + width)
