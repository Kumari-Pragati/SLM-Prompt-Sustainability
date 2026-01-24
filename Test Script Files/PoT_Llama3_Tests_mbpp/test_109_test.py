import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_Equivalent('111', 3), 3)

    def test_edge_case_zero_length(self):
        self.assertEqual(odd_Equivalent('', 5), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_all_ones(self):
        self.assertEqual(odd_Equivalent('11111', 5), 5)

    def test_edge_case_all_zeros(self):
        self.assertEqual(odd_Equivalent('00000', 5), 0)

    def test_edge_case_half_ones(self):
        self.assertEqual(odd_Equivalent('10101', 5), 3)

    def test_edge_case_half_zeros(self):
        self.assertEqual(odd_Equivalent('01010', 5), 2)

    def test_edge_case_all_ones_at_start(self):
        self.assertEqual(odd_Equivalent('111000', 7), 3)

    def test_edge_case_all_ones_at_end(self):
        self.assertEqual(odd_Equivalent('000111', 7), 3)

    def test_edge_case_all_ones_in_middle(self):
        self.assertEqual(odd_Equivalent('000111000', 9), 3)

    def test_edge_case_all_zeros_at_start(self):
        self.assertEqual(odd_Equivalent('000111000', 9), 3)

    def test_edge_case_all_zeros_at_end(self):
        self.assertEqual(odd_Equivalent('111000000', 9), 3)

    def test_edge_case_all_zeros_in_middle(self):
        self.assertEqual(odd_Equivalent('111000000', 9), 3)
