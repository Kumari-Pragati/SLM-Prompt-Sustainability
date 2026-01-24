import unittest
from627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_FirstMissing([], 0, len([])), 1)

    def test_single_element(self):
        self.assertEqual(find_FirstMissing([1], 0, len([1])), None)

    def test_consecutive_elements(self):
        self.assertEqual(find_FirstMissing([1, 2, 3], 0, len([1, 2, 3])), None)

    def test_missing_element_at_start(self):
        self.assertEqual(find_FirstMissing([2, 3, 4], 0, len([2, 3, 4])), 1)

    def test_missing_element_in_middle(self):
        self.assertEqual(find_FirstMissing([1, 2, 4], 0, len([1, 2, 4])), 3)

    def test_missing_element_at_end(self):
        self.assertEqual(find_FirstMissing([1, 2, 5], 0, len([1, 2, 5])), 4)

    def test_missing_element_in_sorted_array(self):
        self.assertEqual(find_FirstMissing([1, 2, 3, 5], 0, len([1, 2, 3, 5])), 4)

    def test_missing_element_in_unsorted_array(self):
        self.assertEqual(find_FirstMissing([3, 5, 2, 1], 0, len([3, 5, 2, 1])), 0)
