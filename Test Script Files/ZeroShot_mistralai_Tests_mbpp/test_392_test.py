import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_get_max_sum_small_numbers(self):
        self.assertEqual(get_max_sum(1), 1)
        self.assertEqual(get_max_sum(2), 2)
        self.assertEqual(get_max_sum(3), 3)
        self.assertEqual(get_max_sum(4), 4)
        self.assertEqual(get_max_sum(5), 6)

    def test_get_max_sum_large_numbers(self):
        self.assertEqual(get_max_sum(10), 29)
        self.assertEqual(get_max_sum(20), 106)
        self.assertEqual(get_max_sum(30), 203)
        self.assertEqual(get_max_sum(40), 355)
        self.assertEqual(get_max_sum(50), 567)

    def test_get_max_sum_edge_cases(self):
        self.assertEqual(get_max_sum(0), 0)
        self.assertEqual(get_max_sum(1000000), 297124566)
