import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Swaps('1010', '0101'), 2)

    def test_edge_case_zero_swaps(self):
        self.assertEqual(min_Swaps('0000', '0000'), 0)

    def test_edge_case_max_swaps(self):
        self.assertEqual(min_Swaps('1111', '0000'), 2)

    def test_edge_case_half_swaps(self):
        self.assertEqual(min_Swaps('1010', '0101'), 2)

    def test_edge_case_half_swaps_reverse(self):
        self.assertEqual(min_Swaps('0101', '1010'), 2)

    def test_edge_case_max_swaps_reverse(self):
        self.assertEqual(min_Swaps('0000', '1111'), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Swaps('1010', 'abc')

    def test_invalid_input_reverse(self):
        with self.assertRaises(TypeError):
            min_Swaps('abc', '1010')
