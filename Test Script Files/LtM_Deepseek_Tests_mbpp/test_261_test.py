import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_simple_division(self):
        self.assertEqual(division_elements((10, 20), (2, 4)), ((5, 5)))

    def test_division_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division_elements((10, 20), (0, 4))

    def test_division_with_empty_tuples(self):
        self.assertEqual(division_elements((), ()), ())

    def test_division_with_single_elements(self):
        self.assertEqual(division_elements((10,), (2,)), ((5,)))

    def test_division_with_negative_numbers(self):
        self.assertEqual(division_elements((-10, 20), (-2, 4)), ((5, -5)))

    def test_division_with_large_numbers(self):
        self.assertEqual(division_elements((10**10, 20**10), (2**10, 4**10)), ((5**10, 5**10)))
