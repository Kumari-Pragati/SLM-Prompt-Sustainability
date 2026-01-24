import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_duplicate("hello world hello"), "hello world")

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(""), "")

    def test_single_word(self):
        self.assertEqual(remove_duplicate("hello"), "hello")

    def test_multiple_duplicates(self):
        self.assertEqual(remove_duplicate("hello hello hello world world world"), "hello world")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_duplicate(123)

    def test_non_string_input_with_error_handling(self):
        # This test case assumes the function handles non-string inputs by raising a TypeError
        # If the function does not raise a TypeError, this test will fail
        self.assertRaises(TypeError, remove_duplicate, 123)
