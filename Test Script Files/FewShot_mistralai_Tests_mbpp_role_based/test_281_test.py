import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_unique_list(self):
        self.assertTrue(all_unique([1, 2, 3, 4]))

    def test_duplicate_list(self):
        self.assertFalse(all_unique([1, 1, 2, 3]))

    def test_empty_list(self):
        self.assertTrue(all_unique([]))

    def test_single_element_list(self):
        self.assertTrue(all_unique([1]))

    def test_list_with_zero(self):
        self.assertTrue(all_unique([0]))

    def test_list_with_negative_numbers(self):
        self.assertTrue(all_unique([-1, -2, -3]))

    def test_list_with_floats(self):
        self.assertTrue(all_unique([1.1, 2.2, 3.3]))

    def test_list_with_strings(self):
        self.assertTrue(all_unique(["a", "b", "c"]))

    def test_list_with_mixed_types(self):
        self.assertFalse(all_unique([1, "a", 2.0]))
