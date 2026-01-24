import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_Substrings('123', 3), 2)
        self.assertEqual(count_Substrings('123', 2), 1)
        self.assertEqual(count_Substrings('123', 1), 1)
        self.assertEqual(count_Substrings('123', 0), 0)

    def test_edge(self):
        self.assertEqual(count_Substrings('', 0), 0)
        self.assertEqual(count_Substrings('0', 1), 1)
        self.assertEqual(count_Substrings('1', 1), 1)
        self.assertEqual(count_Substrings('123456', 10), 6)

    def test_complex(self):
        self.assertEqual(count_Substrings('123456789', 9), 9)
        self.assertEqual(count_Substrings('1234567890', 10), 10)
        self.assertEqual(count_Substrings('123456789012', 12), 12)
