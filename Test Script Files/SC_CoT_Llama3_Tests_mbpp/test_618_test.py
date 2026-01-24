import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_div_list_typical(self):
        self.assertEqual(div_list([10, 2, 5], [2, 1, 0]), [5.0, 5.0, float('inf')])

    def test_div_list_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 2, 5], [0, 1, 0])

    def test_div_list_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 2, 5], [0, 0, 0])

    def test_div_list_division_by_zero_with_negative(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([-10, -2, -5], [0, 0, 0])

    def test_div_list_division_by_zero_with_positive(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 2, 5], [0, 0, 0])

    def test_div_list_division_by_zero_with_mixed(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([-10, 2, -5], [0, 0, 0])

    def test_div_list_division_by_zero_with_mixed_negative(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([-10, -2, -5], [0, 0, 0])

    def test_div_list_division_by_zero_with_mixed_positive(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 2, 5], [0, 0, 0])

    def test_div_list_division_by_zero_with_mixed_negative_positive(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([-10, -2, 5], [0, 0, 0])

    def test_div_list_division_by_zero_with_mixed_negative_negative(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([-10, -2, -5], [0, 0, 0])

    def test_div_list_division_by_zero_with_mixed_positive_positive(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 2, 5], [0, 0, 0])

    def test_div_list_division_by_zero_with_mixed_positive_negative(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 2, -5], [0, 0, 0])

    def test_div_list_division_by_zero_with_mixed_negative_positive(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([-10, 2, 5], [0, 0, 0])
