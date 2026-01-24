import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_Substrings('123', 3), 2)
        self.assertEqual(count_Substrings('000', 3), 1)
        self.assertEqual(count_Substrings('111', 3), 2)

    def test_edge_cases(self):
        self.assertEqual(count_Substrings('123', 1), 0)
        self.assertEqual(count_Substrings('123', 4), 3)
        self.assertEqual(count_Substrings('0123', 4), 3)
        self.assertEqual(count_Substrings('1234', 5), 4)

    def test_boundary_conditions(self):
        self.assertEqual(count_Substrings('', 0), 0)
        self.assertEqual(count_Substrings('1', 1), 1)
        self.assertEqual(count_Substrings('12', 2), 2)
        self.assertEqual(count_Substrings('12345', 5), 4)
        self.assertEqual(count_Substrings('123456', 6), 5)

    def test_complex_cases(self):
        self.assertEqual(count_Substrings('101010', 6), 4)
        self.assertEqual(count_Substrings('01010101', 8), 4)
        self.assertEqual(count_Substrings('1010101010', 10), 5)
        self.assertEqual(count_Substrings('101010101010', 11), 6)
