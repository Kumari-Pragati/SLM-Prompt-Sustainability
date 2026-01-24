import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substrings("123", 3), 2)

    def test_edge_case(self):
        self.assertEqual(count_Substrings("123", 0), 1)

    def test_edge_case2(self):
        self.assertEqual(count_Substrings("123", 1), 1)

    def test_edge_case3(self):
        self.assertEqual(count_Substrings("", 1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Substrings(None, 1)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            count_Substrings("123", None)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            count_Substrings("123", "abc")
