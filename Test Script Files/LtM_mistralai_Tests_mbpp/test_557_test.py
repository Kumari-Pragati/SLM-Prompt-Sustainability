import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):
    def test_simple_uppercase(self):
        self.assertEqual(toggle_string("HELLO"), "hello")

    def test_simple_lowercase(self):
        self.assertEqual(toggle_string("hello"), "HELLO")

    def test_mixed_case(self):
        self.assertEqual(toggle_string("HeLlO wOrLd"), "hello world")

    def test_empty_string(self):
        self.assertEqual(toggle_string(""), "")

    def test_single_character(self):
        self.assertEqual(toggle_string("A"), "a")
        self.assertEqual(toggle_string("a"), "A")

    def test_long_string(self):
        long_string = "ThisIsALongStringThatWeWantToTestTheFunctionWith"
        self.assertEqual(toggle_string(long_string), long_string[::-1])
