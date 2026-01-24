import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(remove_length("hello world", 5), "hello world")
        self.assertEqual(remove_length("a b c d e", 1), "")

    def test_edge_conditions(self):
        self.assertEqual(remove_length("", 0), "")
        self.assertEqual(remove_length(" ", 1), "")
        self.assertEqual(remove_length("a", 1), "a")
        self.assertEqual(remove_length("a ", 1), "a ")
        self.assertEqual(remove_length("a b c", 0), "a b c")

    def test_complex_cases(self):
        self.assertEqual(remove_length("one two three four", 5), "one two three four")
        self.assertEqual(remove_length("one two three four", 6), "one two three four")
        self.assertEqual(remove_length("one two three four", 7), "")
        self.assertEqual(remove_length("one two three four", 0), "one two three four")
