import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(substract_elements((1, 2, 3), (2, 1, 0)), (0, 1, 3))

    def test_subtract_negative_numbers(self):
        self.assertEqual(substract_elements((-1, -2, -3), (-2, -1, 0)), (1, 2, -3))

    def test_subtract_zero(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), (0, 0, 0))

    def test_subtract_empty_tuples(self):
        self.assertEqual(substract_elements((1, 2, 3), ()), (1, 2, 3))
        self.assertEqual(substract_elements((), (1, 2, 3)), (-1, -2, -3))

    def test_subtract_different_length_tuples(self):
        with self.assertRaises(ValueError):
            substract_elements((1, 2, 3), (1, 2))
