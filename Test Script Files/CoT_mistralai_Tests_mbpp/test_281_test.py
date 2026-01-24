import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_single_element(self):
        self.assertTrue(all_unique([1]))

    def test_multiple_elements(self):
        self.assertTrue(all_unique([1, 2, 3]))

    def test_duplicates(self):
        self.assertFalse(all_unique([1, 1, 2, 3]))

    def test_large_list(self):
        self.assertTrue(all_unique(list(range(100))))

    def test_list_with_zero(self):
        self.assertTrue(all_unique([0]))

    def test_list_with_negative_numbers(self):
        self.assertTrue(all_unique([-1, 0, 1]))

    def test_list_with_floats(self):
        self.assertTrue(all_unique([1.0, 2.0, 3.0]))

    def test_list_with_strings(self):
        self.assertTrue(all_unique(["a", "b", "c"]))

    def test_list_with_mixed_types(self):
        self.assertFalse(all_unique([1, "a", 2, "a"]))

    def test_list_with_none(self):
        self.assertTrue(all_unique([None]))

    def test_list_with_empty_string(self):
        self.assertTrue(all_unique([""]))
