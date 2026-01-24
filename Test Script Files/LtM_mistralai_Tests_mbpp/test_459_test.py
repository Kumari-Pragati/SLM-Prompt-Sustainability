import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(remove_uppercase("HelloWorld"), "helloworld")

    def test_empty_input(self):
        self.assertEqual(remove_uppercase(""), "")

    def test_single_uppercase_input(self):
        self.assertEqual(remove_uppercase("HELLO"), "hello")

    def test_multiple_uppercase_input(self):
        self.assertEqual(remove_uppercase("HELLOWORLD"), "helloworld")

    def test_special_characters(self):
        self.assertEqual(remove_uppercase("Hello123World"), "helloworld")

    def test_all_uppercase_input(self):
        self.assertEqual(remove_uppercase("HELLO"), "hello")

    def test_all_lowercase_input(self):
        self.assertEqual(remove_uppercase("helloworld"), "helloworld")
