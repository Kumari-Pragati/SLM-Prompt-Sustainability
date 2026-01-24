import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(add_string([], "Hello"), [])

    def test_single_element_list(self):
        self.assertEqual(add_string([1], "Hello"), ["Hello"])

    def test_multiple_elements_list(self):
        self.assertEqual(add_string([1, 2, 3], "Hello"), ["Hello1", "Hello2", "Hello3"])

    def test_empty_string(self):
        self.assertEqual(add_string([1, 2, 3], ""), [])

    def test_string_with_placeholder(self):
        self.assertEqual(add_string([1, 2, 3], "Hello {}"), ["Hello 1", "Hello 2", "Hello 3"])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            add_string([1, 2, 3], 123)
