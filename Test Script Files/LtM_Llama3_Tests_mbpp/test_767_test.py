import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(get_Pairs_Count([], 0, 0), 0)

    def test_single_element_array(self):
        self.assertEqual(get_Pairs_Count([1], 1, 0), 0)

    def test_no_pairs_found(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3], 3, 4), 0)

    def test_pairs_found(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 3), 1)

    def test_pairs_found_multiple(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 7), 2)

    def test_pairs_found_with_duplicates(self):
        self.assertEqual(get_Pairs_Count([1, 2, 2, 3, 3], 5, 4), 2)

    def test_pairs_found_with_duplicates_and_zero(self):
        self.assertEqual(get_Pairs_Count([1, 2, 2, 3, 3], 5, 0), 0)
