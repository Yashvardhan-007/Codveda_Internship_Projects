"""Unit tests for Codveda Level 1 Task 1."""

import unittest
from decimal import Decimal

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    calculate,
    parse_number,
)


class TestCalculatorOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(Decimal("10"), Decimal("5")), Decimal("15"))

    def test_subtraction(self):
        self.assertEqual(subtract(Decimal("10"), Decimal("5")), Decimal("5"))

    def test_multiplication(self):
        self.assertEqual(multiply(Decimal("10"), Decimal("5")), Decimal("50"))

    def test_division(self):
        self.assertEqual(divide(Decimal("10"), Decimal("5")), Decimal("2"))

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(Decimal("10"), Decimal("0"))

    def test_calculate(self):
        self.assertEqual(
            calculate("1", Decimal("7"), Decimal("3")),
            Decimal("10")
        )

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate("9", Decimal("7"), Decimal("3"))

    def test_parse_number(self):
        self.assertEqual(parse_number("12.50"), Decimal("12.50"))

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            parse_number("hello")


if __name__ == "__main__":
    unittest.main()
