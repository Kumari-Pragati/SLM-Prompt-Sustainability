import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_last_occurrence([], 1), -1)

    def test_single_element(self):
        self.assertEqual(find_last_occurrence([1], 1), 0)
        self.assertEqual(find_last_occurrence([1], 0), -1)

    def test_multiple_elements(self):
        self.assertEqual(find_last_occurrence([1, 2, 1, 3, 1], 1), 4)
        self.assertEqual(find_last_occurrence([1, 2, 1, 3, 1], 2), -1)
        self.assertEqual(find_last_occurrence([1, 2, 1, 3, 1], 3), 3)

    def test_duplicates(self):
        self.assertEqual(find_last_occurrence([1, 1, 2, 1, 3, 1], 1), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_last_occurrence([1, -2, 1, -3, 1], -2), 1)
        self.assertEqual(find_last_occurrence([1, -2, 1, -3, 1], -3), 3)

    def test_not_found(self):
        self.assertEqual(find_last_occurrence([1, 2, 3], 4), -1)

    def test_large_input(self):
        # Test performance with a large list
        large_list = [i for i in range(10000)]
        self.assertEqual(find_last_occurrence(large_list, 9999), 9999)
