import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_simple_division(self):
        self.assertEqual(div_list([1, 2, 3], [4, 5, 6]), [0.25, 0.4, 0.5])

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([1, 2, 3], [0, 0, 0])

    def test_division_with_zero_in_list(self):
        self.assertEqual(div_list([1, 2, 0], [4, 5, 6]), [0.25, 0.4, 0])

    def test_empty_lists(self):
        self.assertEqual(div_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(div_list([2], [1]), [2])

    def test_large_numbers(self):
        self.assertEqual(div_list([10**6, 2*10**6], [10**3, 2*10**3]), [100, 100])

    def test_negative_numbers(self):
        self.assertEqual(div_list([-1, -2, -3], [1, 2, 3]), [-1, -1, -1])
