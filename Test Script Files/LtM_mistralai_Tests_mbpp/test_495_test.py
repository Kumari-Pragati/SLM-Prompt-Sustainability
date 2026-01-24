import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_simple_uppercase(self):
        self.assertEqual(remove_lowercase("HELLO"), "HELLO")

    def test_simple_mixedcase(self):
        self.assertEqual(remove_lowercase("HelloWorld"), "HelloWorld")

    def test_empty_string(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_single_lowercase(self):
        self.assertEqual(remove_lowercase("hello"), "")

    def test_multiple_lowercase(self):
        self.assertEqual(remove_lowercase("helloWorld123"), "World123")

    def test_min_length_string(self):
        self.assertEqual(remove_lowercase("A"), "A")

    def test_max_length_string(self):
        self.assertEqual(remove_lowercase("Z" * 26), "Z" * 26)
