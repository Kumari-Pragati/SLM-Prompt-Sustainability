import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(get_Pairs_Count([], 0, 0), 0)

    def test_single_element_array(self):
        self.assertEqual(get_Pairs_Count([1], 1, 1), 0)
        self.assertEqual(get_Pairs_Count([2], 1, 2), 0)
        self.assertEqual(get_Pairs_Count([-1], 1, -1), 0)

    def test_two_elements_array(self):
        self.assertEqual(get_Pairs_Count([1, 2], 2, 3), 0)
        self.assertEqual(get_Pairs_Count([1, 2], 2, 1), 0)
        self.assertEqual(get_Pairs_Count([1, 2], 2, 3), 0)
        self.assertEqual(get_Pairs_Count([2, 1], 2, 3), 0)
        self.assertEqual(get_Pairs_Count([1, 1], 2, 2), 1)
        self.assertEqual(get_Pairs_Count([-1, 1], 2, 0), 1)

    def test_multiple_elements_array(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 5), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 6), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 7), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 5), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 6), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 4), 3)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 5), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 6), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 7), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 8), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 9), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 10), 2)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 11), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 12), 1)

    def test_negative_numbers(self):
        self.assertEqual(get_Pairs_Count([-1, -2, -3, -4], 4, 5), 0)
        self.assertEqual(get_Pairs_Count([-1, -2, -3, -4], 4, 0), 6)
        self.assertEqual(get_Pairs_Count([-1, -2, -3, -4], 4, -1), 4)
        self.assertEqual(get_Pairs_Count([-1, -2, -3, -4], 4, 1), 0)
        self.assertEqual(get_Pairs_Count([-1, -2, -3, -4], 4, 2), 3)
        self.assertEqual(get_Pairs_Count([-1, -2, -3, -4], 4,