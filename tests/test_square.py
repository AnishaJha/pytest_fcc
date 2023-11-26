import pytest

import source.shapes as shapes


@pytest.mark.parametrize("side, area", [(5, 25), (6, 36), (9, 81), (10, 100)])
def test_multiple_square_area(side, area):
    assert shapes.Square(side).area() == area


@pytest.mark.parametrize("side, perimeter", [(5, 20), (6, 24), (2, 8), (7, 28)])
def test_multiple_perimeter(side, perimeter):
    assert shapes.Square(side).perimeter() == perimeter
