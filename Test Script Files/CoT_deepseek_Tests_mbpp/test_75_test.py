import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(10, 20, 30), (4, 8, 12), (15, 25, 35)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[(10, 20, 30), (15, 25, 35)]')

    def test_empty_list(self):
        test_list = []
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[]')

    def test_all_divisible(self):
        test_list = [(10, 20, 30), (4, 8, 12), (15, 25, 35)]
        K = 1
        self.assertEqual(find_tuples(test_list, K), '[(10, 20, 30), (4, 8, 12), (15, 25, 35)]')

    def test_no_divisible(self):
        test_list = [(11, 21, 31), (5, 10, 15), (22, 44, 66)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[]')

    def test_negative_numbers(self):
        test_list = [(-10, -20, -30), (-4, -8, -12), (-15, -25, -35)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[]')

    def test_zero_in_list(self):
        test_list = [(0, 20, 30), (4, 8, 12), (15, 25, 35)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[(0, 20, 30), (15, 25, 35)]')

    def test_zero_as_K(self):
        test_list = [(10, 20, 30), (4, 8, 12), (15, 25, 35)]
        K = 0
        self.assertRaises(ZeroDivisionError, find_tuples, test_list, K)
