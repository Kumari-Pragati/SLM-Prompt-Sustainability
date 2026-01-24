import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_long_word("Hello world"), ["Hello"])
        self.assertEqual(find_long_word("Python is fun"), ["Python"])

    def test_edge_conditions(self):
        self.assertEqual(find_long_word(""), [])
        self.assertEqual(find_long_word("a"), [])
        self.assertEqual(find_long_word("123456"), ["12345"])

    def test_complex_cases(self):
        self.assertEqual(find_long_word("Hello world! This is a test."), ["Hello", "world", "This", "test"])
        self.assertEqual(find_long_word("Python3 is a great language!"), ["Python3"])
