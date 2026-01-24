import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_Equivalent('10101', 5), 3)
        self.assertEqual(odd_Equivalent('11111', 5), 5)
        self.assertEqual(odd_Equivalent('00000', 5), 0)

    def test_edge_case_short_string(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_zero_length(self):
        self.assertEqual(odd_Equivalent('', 0), 0)

    def test_edge_case_negative_n(self):
        self.assertRaises(ValueError, odd_Equivalent, '1', -1)

    def test_corner_case_empty_string_and_zero_n(self):
        self.assertEqual(odd_Equivalent('', 0), 0)
