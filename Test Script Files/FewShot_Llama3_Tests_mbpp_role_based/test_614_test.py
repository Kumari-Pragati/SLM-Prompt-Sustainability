import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(cummulative_sum(test_list), 45)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(cummulative_sum(test_list), 0)

    def test_single_element_list(self):
        test_list = [[1, 2, 3]]
        self.assertEqual(cummulative_sum(test_list), 6)

    def test_list_with_single_element_sublists(self):
        test_list = [[1], [2, 3], [4, 5, 6]]
        self.assertEqual(cummulative_sum(test_list), 21)

    def test_list_with_empty_sublists(self):
        test_list = [[], [1, 2, 3], [4, 5, 6]]
        self.assertEqual(cummulative_sum(test_list), 21)
