class Figure:

    def __init__(self, name, area, perimeter ):
        self.name = name
        self.area = area
        self.perimeter = perimeter

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        general_area = self.area + figure.area
        return general_area



