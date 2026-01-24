import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(division_elements((2, 4, 6), (1, 2, 3)), (2, 2, 2))
        self.assertEqual(division_elements((-2, 4, -6), (1, 2, -3)), (-2, 2, -2))

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, lambda: division_elements((0, 4, 0), (1, 0, 0)))

    def test_mixed_types(self):
        self.assertRaises(TypeError, lambda: division_elements((2, 'a', 6), (1, 2, 3)))

    def test_different_lengths(self):
        self.assertRaises(ValueError, lambda: division_elements((2, 4, 6), (1, 2)))
