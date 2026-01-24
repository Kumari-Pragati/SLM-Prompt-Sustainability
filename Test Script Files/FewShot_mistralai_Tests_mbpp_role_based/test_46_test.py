import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element(self):
        self.assertTrue(test_distinct([1]))

    def test_duplicates(self):
        self.assertFalse(test_distinct([1, 1]))

    def test_unique_elements(self):
        self.assertTrue(test_distinct([1, 2, 3]))

    def test_negative_numbers(self):
        self.assertTrue(test_distinct([-1, -2, -3]))

    def test_mixed_numbers(self):
        self.assertTrue(test_distinct([1, -2, 3]))

    def test_floats(self):
        self.assertTrue(test_distinct([1.0, 2.0, 3.0]))

    def test_strings(self):
        self.assertTrue(test_distinct(["a", "b", "c"]))

    def test_mixed_types(self):
        self.assertTrue(test_distinct([1, "a", 3]))

    def test_empty_string(self):
        self.assertTrue(test_distinct([]))
