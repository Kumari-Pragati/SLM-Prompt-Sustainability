import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(remove_extra_char("Hello_World"), "HelloWorld")
        self.assertEqual(remove_extra_char("123_456"), "123456")
        self.assertEqual(remove_extra_char("_Hello_World_"), "")

    def test_edge_input(self):
        self.assertEqual(remove_extra_char(""), "")
        self.assertEqual(remove_extra_char("_"), "")
        self.assertEqual(remove_extra_char("Hello_"), "Hello")
        self.assertEqual(remove_extra_char("_World"), "World")

    def test_complex_input(self):
        self.assertEqual(remove_extra_char("Hello_World_123_456"), "HelloWorld123456")
        self.assertEqual(remove_extra_char("_Hello_World_123_456_"), "HelloWorld123456")
        self.assertEqual(remove_extra_char("Hello_World_123_456_Hello"), "HelloWorld123456Hello")
        self.assertEqual(remove_extra_char("_Hello_World_123_456_Hello_"), "HelloWorld123456Hello")
