import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):

    def test_simple_even_array(self):
        self.assertEqual(min_Num([0, 2, 4], 3), 2)

    def test_simple_odd_array(self):
        self.assertEqual(min_Num([1, 3, 5], 3), 1)

    def test_single_element(self):
        self.assertEqual(min_Num([3], 1), 2)

    def test_empty_array(self):
        self.assertEqual(min_Num([], 0), None)

    def test_negative_numbers(self):
        self.assertEqual(min_Num([-1, -3, -5], 3), 1)

    def test_zero(self):
        self.assertEqual(min_Num([0], 1), 2)

    def test_max_int(self):
        self.assertEqual(min_Num([2147483647], 1), 2)

    def test_min_int(self):
        self.assertEqual(min_Num([-2147483648], 1), 1)
