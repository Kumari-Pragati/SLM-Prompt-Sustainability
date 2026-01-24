import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_Equivalent('1011', 4), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(odd_Equivalent('', 0), 0)

    def test_boundary_case_single_character(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_boundary_case_multiple_characters(self):
        self.assertEqual(odd_Equivalent('1111', 4), 4)
        self.assertEqual(odd_Equivalent('0000', 4), 0)

    def test_corner_case_all_ones(self):
        self.assertEqual(odd_Equivalent('1111111111', 10), 10)

    def test_corner_case_all_zeros(self):
        self.assertEqual(odd_Equivalent('0000000000', 10), 0)

    def test_corner_case_mixed_ones_and_zeros(self):
        self.assertEqual(odd_Equivalent('1010101010', 10), 5)
