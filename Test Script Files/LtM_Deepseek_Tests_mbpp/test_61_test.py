import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(count_Substrings("131", 3), 2)
        self.assertEqual(count_Substrings("123", 3), 1)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(count_Substrings("", 0), 0)
        self.assertEqual(count_Substrings("1", 1), 0)
        self.assertEqual(count_Substrings("0", 1), 0)
        self.assertEqual(count_Substrings("1234567890", 10), 45)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(count_Substrings("1111111111", 10), 55)
        self.assertEqual(count_Substrings("0000000000", 10), 0)
        self.assertEqual(count_Substrings("1010101010", 10), 45)
