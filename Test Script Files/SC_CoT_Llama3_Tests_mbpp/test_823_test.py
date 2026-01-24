import unittest
from mbpp_823_code import check_substring

class TestCheckSubstring(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(check_substring("Hello, world!", "world"), "string starts with the given substring")
        self.assertEqual(check_substring("Python is awesome", "Python"), "string starts with the given substring")
        self.assertEqual(check_substring("This is a test", "test"), "string starts with the given substring")

    def test_edge_cases(self):
        self.assertEqual(check_substring("Hello, world!", "hello"), "string doesnt start with the given substring")
        self.assertEqual(check_substring("Python is awesome", "awesome"), "string doesnt start with the given substring")
        self.assertEqual(check_substring("This is a test", "This"), "string starts with the given substring")

    def test_boundary_cases(self):
        self.assertEqual(check_substring("Hello, world!", "Hello"), "string starts with the given substring")
        self.assertEqual(check_substring("Python is awesome", "is"), "string doesnt start with the given substring")
        self.assertEqual(check_substring("This is a test", "a"), "string doesnt start with the given substring")

    def test_special_cases(self):
        self.assertEqual(check_substring("Hello, world!", "world!"), "string doesnt start with the given substring")
        self.assertEqual(check_substring("Python is awesome", "python"), "string doesnt start with the given substring")
        self.assertEqual(check_substring("This is a test", "test!"), "string doesnt start with the given substring")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_substring(123, "test")
        with self.assertRaises(TypeError):
            check_substring("test", 123)
