import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(div_list([10, 20, 30], [2, 4, 5]), [5.0, 5.0, 6.0])

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 20, 30], [0, 4, 5])

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 20, 30], [2, 0, 5])

    def test_division_by_zero_list(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 20, 30], [2, 0, 5, 0])

    def test_empty_lists(self):
        self.assertEqual(div_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(div_list([10], [2]), [5.0])
        self.assertEqual(div_list([10], []), [])

    def test_division_by_negative(self):
        self.assertEqual(div_list([-10, 20, 30], [-2, 4, 5]), [-5.0, 5.0, 6.0])

    def test_division_by_positive(self):
        self.assertEqual(div_list([10, 20, 30], [2, 4, 5]), [5.0, 5.0, 6.0])
