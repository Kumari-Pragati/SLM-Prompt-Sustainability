import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(division_elements((10, 20, 30), (2, 4, 6)), ((5, 5, 5)))

    def test_single_element(self):
        self.assertEqual(division_elements((10,), (2,)), ((5,)))

    def test_empty_tuples(self):
        self.assertEqual(division_elements((), ()), ())

    def test_negative_numbers(self):
        self.assertEqual(division_elements((-10, -20, -30), (2, 4, 6)), ((-5, -5, -5)))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((10, 20, 30), (0, 4, 6))

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            division_elements((10, 20, 30), (2, 4))
