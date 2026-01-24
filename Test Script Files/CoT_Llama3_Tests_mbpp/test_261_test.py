import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(division_elements((10, 2), (20, 4)), (5, 5))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((10, 0), (20, 4))

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((0, 2), (20, 4))

    def test_division_by_negative(self):
        self.assertEqual(division_elements((-10, 2), (-20, 4)), (-5, -5))

    def test_division_by_positive(self):
        self.assertEqual(division_elements((10, 2), (20, 4)), (5, 5))

    def test_division_by_zero_negative(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((-10, 0), (-20, 4))

    def test_division_by_zero_positive(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((10, 0), (20, 4))

    def test_division_by_negative_negative(self):
        self.assertEqual(division_elements((-10, -2), (-20, -4)), (5, 5))

    def test_division_by_positive_positive(self):
        self.assertEqual(division_elements((10, 2), (20, 4)), (5, 5))

    def test_division_by_negative_positive(self):
        self.assertEqual(division_elements((-10, 2), (-20, 4)), (-5, -5))

    def test_division_by_positive_negative(self):
        self.assertEqual(division_elements((10, -2), (20, -4)), (-5, -5))
