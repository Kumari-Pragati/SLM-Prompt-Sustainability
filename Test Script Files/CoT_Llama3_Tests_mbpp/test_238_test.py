import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(number_of_substrings("abc"), 3)
        self.assertEqual(number_of_substrings("abcd"), 6)
        self.assertEqual(number_of_substrings("abcde"), 6)

    def test_edge_cases(self):
        self.assertEqual(number_of_substrings(""), 0)
        self.assertEqual(number_of_substrings("a"), 1)
        self.assertEqual(number_of_substrings("a" * 100), 4950)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            number_of_substrings(123)
        with self.assertRaises(TypeError):
            number_of_substrings([1, 2, 3])
