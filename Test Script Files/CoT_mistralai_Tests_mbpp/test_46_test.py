import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(test_distinct([]))

    def test_single_element(self):
        self.assertTrue(test_distinct([1]))

    def test_multiple_elements(self):
        self.assertTrue(test_distinct([1, 2, 3]))
        self.assertTrue(test_distinct([3, 2, 1]))

    def test_duplicates(self):
        self.assertFalse(test_distinct([1, 1, 2]))
        self.assertFalse(test_distinct([1, 2, 1]))

    def test_negative_numbers(self):
        self.assertTrue(test_distinct([1, -2, 3]))

    def test_floats(self):
        self.assertTrue(test_distinct([1.0, 2.0, 3.0]))

    def test_strings(self):
        self.assertTrue(test_distinct(["a", "b", "c"]))

    def test_mixed_types(self):
        self.assertRaises(TypeError, test_distinct, [1, "a", 3.0])

    def test_empty_string(self):
        self.assertTrue(test_distinct(""))

    def test_single_character_string(self):
        self.assertTrue(test_distinct("a"))

    def test_multiple_characters_string(self):
        self.assertTrue(test_distinct("abc"))
        self.assertTrue(test_distinct("cba"))
