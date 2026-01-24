import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Substrings("123", 3), 2)
        self.assertEqual(count_Substrings("0123", 4), 3)
        self.assertEqual(count_Substrings("1010", 4), 2)
        self.assertEqual(count_Substrings("1234", 4), 3)
        self.assertEqual(count_Substrings("001010", 6), 3)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Substrings("1", 1), 1)
        self.assertEqual(count_Substrings("12", 2), 1)
        self.assertEqual(count_Substrings("12345", 5), 4)
        self.assertEqual(count_Substrings("123456", 6), 5)
        self.assertEqual(count_Substrings("1234567", 7), 6)
        self.assertEqual(count_Substrings("12345678", 8), 7)
        self.assertEqual(count_Substrings("123456789", 9), 8)
        self.assertEqual(count_Substrings("1234567890", 10), 9)

        self.assertEqual(count_Substrings("0", 1), 0)
        self.assertEqual(count_Substrings("00", 2), 1)
        self.assertEqual(count_Substrings("000", 3), 2)
        self.assertEqual(count_Substrings("0000", 4), 3)
        self.assertEqual(count_Substrings("00000", 5), 4)
        self.assertEqual(count_Substrings("000000", 6), 5)
        self.assertEqual(count_Substrings("0000000", 7), 6)
        self.assertEqual(count_Substrings("00000000", 8), 7)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Substrings, 1, 2)
        self.assertRaises(TypeError, count_Substrings, "abc", 2)
        self.assertRaises(TypeError, count_Substrings, "123", 0)
