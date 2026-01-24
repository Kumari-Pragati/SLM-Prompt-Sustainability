import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element(self):
        self.assertTrue(test_distinct([1]))

    def test_multiple_unique_elements(self):
        self.assertTrue(test_distinct([1, 2, 3]))

    def test_multiple_duplicate_elements(self):
        self.assertFalse(test_distinct([1, 1, 2]))

    def test_negative_numbers(self):
        self.assertTrue(test_distinct([-1, -2, -3]))

    def test_mixed_types(self):
        self.assertFalse(test_distinct([1, 'a', 2]))

    def test_empty_string(self):
        self.assertTrue(test_distinct([]))

    def test_single_character_string(self):
        self.assertTrue(test_distinct(['a']))

    def test_multiple_unique_characters_string(self):
        self.assertTrue(test_distinct(['a', 'b', 'c']))

    def test_multiple_duplicate_characters_string(self):
        self.assertFalse(test_distinct(['a', 'a', 'b']))
