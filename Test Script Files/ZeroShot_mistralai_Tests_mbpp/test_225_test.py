import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):

    def test_find_min_empty_list(self):
        self.assertIsNone(find_Min([], 0, len([])))

    def test_find_min_single_element(self):
        self.assertEqual(find_Min([1], 0, len([1])), 1)

    def test_find_min_multiple_elements(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, len([1, 2, 3, 4, 5])), 1)
        self.assertEqual(find_Min([5, 4, 3, 2, 1], 0, len([5, 4, 3, 2, 1])), 1)
        self.assertEqual(find_Min([1, 1, 2, 3, 4, 5], 0, len([1, 1, 2, 3, 4, 5])), 1)

    def test_find_min_duplicates(self):
        self.assertEqual(find_Min([1, 1, 2, 2, 3, 4, 5], 0, len([1, 1, 2, 2, 3, 4, 5])), 1)
        self.assertEqual(find_Min([1, 1, 1, 2, 3, 4, 5], 0, len([1, 1, 1, 2, 3, 4, 5])), 1)

    def test_find_min_unsorted_list(self):
        self.assertEqual(find_Min([5, 3, 2, 1], 0, len([5, 3, 2, 1])), 1)
        self.assertEqual(find_Min([5, 3, 2, 1, 4], 0, len([5, 3, 2, 1, 4])), 1)
        self.assertEqual(find_Min([5, 3, 2, 1, 4, 6], 0, len([5, 3, 2, 1, 4, 6])), 1)
