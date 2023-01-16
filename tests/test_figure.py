from src.Triangle import Triangle
from src.Square import Square
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Circle import Circle
import src.Integration_module
import pytest

def test_triangle_right_area():
    triangle = Triangle(13, 14, 15)
    assert triangle.area == 84,"Triangle area is right"

def test_triangle_right_perimeter():
    triangle = Triangle(13, 14, 15)
    assert triangle.perimeter == 42,"Triangle perimeter is right"

def test_not_figure():
    with pytest.raises(ValueError):
        triangle = Triangle(13, 14, 15)
        triangle.add_area("не фигура")

def test_square_right_area():
    square = Square(10)
    assert square.area == 100,"Square area is right"

def test_add_area_square_by_triangle():
    triangle = Triangle(13, 14, 15)
    square = Square(10)
    assert triangle.add_area(square) == 184, "Add area square by triangle"

def test_add_area_square_by_rectangle():
    rectangle = Rectangle(5, 10)
    square = Square(10)
    assert rectangle.add_area(square) == 150, "Add area square by rectangle"




