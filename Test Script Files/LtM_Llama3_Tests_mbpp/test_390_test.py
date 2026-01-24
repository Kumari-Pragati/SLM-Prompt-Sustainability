import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(add_string([1, 2, 3], "Hello {}"), ["Hello 1", "Hello 2", "Hello 3"])

    def test_empty_list(self):
        self.assertEqual(add_string([], "Hello {}"), [])

    def test_empty_string(self):
        self.assertEqual(add_string([1, 2, 3], ""), [])

    def test_single_element_list(self):
        self.assertEqual(add_string([1], "Hello {}"), ["Hello 1"])

    def test_single_element_string(self):
        self.assertEqual(add_string([1, 2, 3], "Hello"), ["Hello"])

    def test_multiple_strings(self):
        self.assertEqual(add_string([1, 2, 3], "Hello {} World {}"), ["Hello 1 World 1", "Hello 2 World 2", "Hello 3 World 3"])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_string("string", "Hello {}")
