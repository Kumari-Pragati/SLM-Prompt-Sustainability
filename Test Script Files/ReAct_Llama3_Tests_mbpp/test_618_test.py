import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_div_list_typical(self):
        self.assertEqual(div_list([10, 20, 30], [2, 4, 5]), [5.0, 5.0, 6.0])

    def test_div_list_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 20, 30], [0, 4, 5])

    def test_div_list_empty_list(self):
        self.assertEqual(div_list([], [1, 2, 3]), [])

    def test_div_list_single_element(self):
        self.assertEqual(div_list([10], [2]), [5.0])

    def test_div_list_single_element_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10], [0])

    def test_div_list_single_element_list(self):
        self.assertEqual(div_list([10], []), [])

    def test_div_list_multiple_lists(self):
        self.assertEqual(div_list([10, 20, 30], [2, 4, 5]), [5.0, 5.0, 6.0])

    def test_div_list_multiple_lists_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 20, 30], [0, 4, 5])
