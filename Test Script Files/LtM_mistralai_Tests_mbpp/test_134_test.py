import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_simple_even_array(self):
        self.assertEqual(check_last([0, 2, 4], 3, 0), 'EVEN')

    def test_simple_odd_array(self):
        self.assertEqual(check_last([1, 3, 5], 3, 1), 'ODD')

    def test_empty_array(self):
        self.assertEqual(check_last([], 0, 0), 'EVEN')

    def test_single_element_array(self):
        self.assertEqual(check_last([1], 1, 0), 'EVEN')
        self.assertEqual(check_last([2], 1, 1), 'ODD')

    def test_min_max_values(self):
        self.assertEqual(check_last([-2147483648, -1, 0, 1, 2147483647], 5, 0), 'EVEN')

    def test_negative_array(self):
        self.assertEqual(check_last([-1, -2, -3], 3, 0), 'EVEN')

    def test_negative_odd_array(self):
        self.assertEqual(check_last([-1, -3, -5], 3, 1), 'ODD')
