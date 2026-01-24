import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(get_Pairs_Count([], 0, 0), 0)

    def test_single_element_array(self):
        self.assertEqual(get_Pairs_Count([1], 1, 0), 0)

    def test_no_pairs_found(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 5), 0)

    def test_pairs_found(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5, 6], 6, 7), 2)

    def test_pairs_found_with_duplicates(self):
        self.assertEqual(get_Pairs_Count([1, 2, 2, 3, 4, 5, 6], 7, 7), 3)

    def test_pairs_found_with_duplicates_and_zero_sum(self):
        self.assertEqual(get_Pairs_Count([1, 2, 2, 3, 4, 5, 6], 7, 0), 2)
