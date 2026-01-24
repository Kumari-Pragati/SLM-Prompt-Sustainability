import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_Swaps('0110', '1110'), 2)

    def test_edge_case_zero_swaps(self):
        self.assertEqual(min_Swaps('0000', '0000'), 0)

    def test_edge_case_all_swaps(self):
        self.assertEqual(min_Swaps('1111', '0000'), 4)

    def test_edge_case_half_swaps(self):
        self.assertEqual(min_Swaps('1010', '0101'), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Swaps('abc', 'def')
