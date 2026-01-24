import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(check_occurences([]), {})

    def test_single_element_list(self):
        self.assertEqual(check_occurences([1]), {tuple(sorted([1])): 1})

    def test_multiple_elements_list(self):
        self.assertEqual(check_occurences([1, 2, 3]), {tuple(sorted([1, 2, 3])): 1})

    def test_duplicates_in_list(self):
        self.assertEqual(check_occurences([1, 2, 2, 3, 3, 3]), {tuple(sorted([1, 2, 2, 3, 3, 3])): 3})

    def test_empty_list_with_duplicates(self):
        self.assertEqual(check_occurences([1, 1, 2, 2, 2]), {tuple(sorted([1, 1, 2, 2, 2])): 3})

    def test_list_with_negative_numbers(self):
        self.assertEqual(check_occurences([-1, -2, -3]), {tuple(sorted([-1, -2, -3])): 1})

    def test_list_with_negative_and_positive_numbers(self):
        self.assertEqual(check_occurences([-1, -2, 1, 2, 3]), {tuple(sorted([-1, -2, 1, 2, 3])): 1})
