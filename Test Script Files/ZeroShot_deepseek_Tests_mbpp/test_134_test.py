import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_even_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "ODD")
        self.assertEqual(check_last([10, 20, 30, 40, 50], 5, 1), "EVEN")

    def test_odd_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4, 6], 5, 1), "EVEN")
        self.assertEqual(check_last([10, 20, 30, 40, 51], 5, 1), "ODD")

    def test_p_not_equal_to_1(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 0), "EVEN")
        self.assertEqual(check_last([10, 20, 30, 40, 50], 5, 0), "EVEN")
