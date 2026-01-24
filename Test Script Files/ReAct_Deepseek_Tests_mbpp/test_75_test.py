import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(10, 20, 30), (4, 8, 12), (5, 10, 15)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[(10, 20, 30), (5, 10, 15)]')

    def test_empty_list(self):
        test_list = []
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[]')

    def test_all_zero(self):
        test_list = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[(0, 0, 0), (0, 0, 0), (0, 0, 0)]')

    def test_no_divisible_elements(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[]')

    def test_negative_elements(self):
        test_list = [(-10, -20, -30), (-4, -8, -12), (-5, -10, -15)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[]')

    def test_large_elements(self):
        test_list = [(1000, 2000, 3000), (4000, 5000, 6000), (7000, 8000, 9000)]
        K = 5
        self.assertEqual(find_tuples(test_list, K), '[(1000, 2000, 3000), (4000, 5000, 6000), (7000, 8000, 9000)]')
