import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_all_ints(self):
        self.assertEqual(sort_mixed_list([4, 2, 1, 3]), [1, 2, 3, 4])

    def test_all_strings(self):
        self.assertEqual(sort_mixed_list(["apple", "banana", "cherry"]), ["apple", "banana", "cherry"])

    def test_mixed_list(self):
        self.assertEqual(sort_mixed_list([4, "apple", 2, "banana", 1, "cherry"]), [1, "apple", 2, "banana", 4, "cherry"])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_mixed_list([4, "apple", 2, "banana", 1, "apple"]), [1, "apple", 2, "banana", 4])
