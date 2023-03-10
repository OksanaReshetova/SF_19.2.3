import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6# умножение

    def test_devision_calculator_correctly(self):
        assert self.calc.devision(self, 8, 4) == 2# деление

    def test_subtraction_calculator_correctly(self):
        assert self.calc.subtraction(self, 10, 7) == 3# вычитание

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 1, 5) == 6# сложение



