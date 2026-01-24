import unittest
from mbpp_61_code import defaultdict
from your_module import count_Substrings  # replace 'your_module' with the actual module name where the function is defined

class TestCountSubstrings(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substrings("", 0), 1)

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(count_Substrings(char, len(char)), 1)

    def test_simple_strings(self):
        self.assertEqual(count_Substrings("0", 1), 1)
        self.assertEqual(count_Substrings("1", 1), 1)
        self.assertEqual(count_Substrings("00", 2), 2)
        self.assertEqual(count_Substrings("10", 2), 2)
        self.assertEqual(count_Substrings("01", 2), 3)
        self.assertEqual(count_Substrings("11", 2), 3)

    def test_complex_strings(self):
        self.assertEqual(count_Substrings("01010101", 8), 10)
        self.assertEqual(count_Substrings("10101010", 8), 10)
        self.assertEqual(count_Substrings("01101010", 8), 9)
        self.assertEqual(count_Substrings("10110101", 8), 9)
