import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_even_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "EVEN")

    def test_odd_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "ODD")

    def test_even_sum_p_0(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 0), "EVEN")

    def test_even_sum_p_1(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "EVEN")

    def test_even_sum_p_2(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 2), "EVEN")

    def test_odd_sum_p_1(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "ODD")

    def test_odd_sum_p_2(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 2), "EVEN")
