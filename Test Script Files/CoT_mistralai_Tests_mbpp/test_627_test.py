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

    def test_missing_element_at_end(self):
        self.assertEqual(find_FirstMissing([1, 2, 3], 0, len([1, 2, 3]) - 1), 4)

    def test_missing_element_in_middle(self):
        self.assertEqual(find_FirstMissing([1, 2, 4], 0, len([1, 2, 4])), 3)

    def test_duplicate_elements(self):
        self.assertEqual(find_FirstMissing([1, 1, 2, 3], 0, len([1, 1, 2, 3])), None)

    def test_invalid_start_greater_than_end(self):
        self.assertEqual(find_FirstMissing([1, 2, 3], 5, 0), 1)

    def test_invalid_negative_start(self):
        self.assertEqual(find_FirstMissing([1, 2, 3], -1, len([1, 2, 3])), None)

    def test_invalid_negative_end(self):
        self.assertEqual(find_FirstMissing([1, 2, 3], len([1, 2, 3]) + 1, 0), len([1, 2, 3]) + 1)
