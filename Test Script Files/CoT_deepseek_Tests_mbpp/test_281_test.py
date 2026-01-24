import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(all_unique([1, 2, 3, 4]))

    def test_typical_case_with_duplicates(self):
        self.assertFalse(all_unique([1, 2, 2, 3, 4]))

    def test_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_single_element(self):
        self.assertTrue(all_unique([1]))

    def test_duplicate_element(self):
        self.assertFalse(all_unique([1, 1]))

    def test_large_list(self):
        self.assertTrue(all_unique(list(range(1, 10001))))

    def test_large_list_with_duplicates(self):
        self.assertFalse(all_unique([1] * 10001))

    def test_negative_numbers(self):
        self.assertTrue(all_unique([-1, -2, -3, -4]))

    def test_negative_numbers_with_duplicates(self):
        self.assertFalse(all_unique([-1, -2, -2, -3, -4]))

    def test_mixed_numbers(self):
        self.assertTrue(all_unique([1, -2, 3, -4]))

    def test_mixed_numbers_with_duplicates(self):
        self.assertFalse(all_unique([1, -2, -2, 3, -4]))

    def test_non_integer_elements(self):
        self.assertTrue(all_unique(['a', 'b', 'c', 'd']))

    def test_non_integer_elements_with_duplicates(self):
        self.assertFalse(all_unique(['a', 'b', 'b', 'c', 'd']))
