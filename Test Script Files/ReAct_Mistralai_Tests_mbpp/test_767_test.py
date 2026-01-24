import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(get_Pairs_Count([], 0, 10), 0)

    def test_single_element_array(self):
        self.assertEqual(get_Pairs_Count([1], 1, 10), 0)
        self.assertEqual(get_Pairs_Count([5], 1, 10), 0)

    def test_pair_in_array(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 5), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 6), 0)

    def test_sum_greater_than_array_sum(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 10), 0)

    def test_sum_less_than_array_min(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 0), 0)

    def test_duplicate_elements(self):
        self.assertEqual(get_Pairs_Count([1, 1, 2, 3, 4], 5, 2), 1)
