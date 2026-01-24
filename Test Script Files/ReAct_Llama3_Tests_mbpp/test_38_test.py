import unittest
from mbpp_38_code import div_even_odd

class TestDivEvenOdd(unittest.TestCase):

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_even_odd([4, 5])

    def test_division_by_nonzero(self):
        self.assertEqual(div_even_odd([4, 5]), 4/5)

    def test_no_even_numbers(self):
        with self.assertRaises(ValueError):
            div_even_odd([1, 3, 5])

    def test_no_odd_numbers(self):
        with self.assertRaises(ValueError):
            div_even_odd([2, 4, 6])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            div_even_odd([])

    def test_single_element_list(self):
        with self.assertRaises(ValueError):
            div_even_odd([2])
