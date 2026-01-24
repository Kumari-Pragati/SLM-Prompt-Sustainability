import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_Pairs_Count([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(get_Pairs_Count([1], 1, 1), 0)
        self.assertEqual(get_Pairs_Count([1], 1, 2), 0)

    def test_simple_pairs(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 5), 2)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 6), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 7), 0)

    def test_multiple_pairs(self):
        self.assertEqual(get_Pairs_Count([1, 1, 2, 2, 3, 3, 4, 4], 8, 5), 4)
        self.assertEqual(get_Pairs_Count([1, 1, 2, 2, 3, 3, 4, 4], 8, 6), 3)
        self.assertEqual(get_Pairs_Count([1, 1, 2, 2, 3, 3, 4, 4], 8, 7), 2)
        self.assertEqual(get_Pairs_Count([1, 1, 2, 2, 3, 3, 4, 4], 8, 8), 4)

    def test_negative_numbers(self):
        self.assertEqual(get_Pairs_Count([-1, -2, 3, 4], 4, 0), 1)
        self.assertEqual(get_Pairs_Count([-1, -2, 3, 4], 4, 1), 1)
        self.assertEqual(get_Pairs_Count([-1, -2, 3, 4], 4, -1), 0)
        self.assertEqual(get_Pairs_Count([-1, -2, 3, 4], 4, -2), 0)
