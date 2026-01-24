import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):
    def test_simple_division(self):
        self.assertEqual(division_elements((10, 2), (20, 4)), (5, 5))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((10, 0), (20, 4))

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            division_elements([], [1, 2, 3])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            division_elements([1, 2, 3], ['a', 'b', 'c'])

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((10, 0), (20, 0))

    def test_division_by_negative(self):
        self.assertEqual(division_elements((-10, 2), (-20, 4)), (-5, -5))

    def test_division_by_positive(self):
        self.assertEqual(division_elements((10, 2), (20, 4)), (5, 5))
