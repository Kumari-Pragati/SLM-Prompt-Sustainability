import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps('0101', '1010'), 1)

    def test_typical_case_with_more_swaps(self):
        self.assertEqual(min_Swaps('010101', '101010'), 2)

    def test_typical_case_with_less_swaps(self):
        self.assertEqual(min_Swaps('0101', '0101'), 0)

    def test_edge_case_with_empty_strings(self):
        self.assertEqual(min_Swaps('', ''), 0)

    def test_edge_case_with_same_string(self):
        self.assertEqual(min_Swaps('0101', '0101'), 0)

    def test_edge_case_with_strings_of_different_lengths(self):
        self.assertEqual(min_Swaps('0101', '101'), -1)

    def test_error_case_with_non_string_inputs(self):
        with self.assertRaises(TypeError):
            min_Swaps(1234, '1010')

    def test_error_case_with_strings_of_different_lengths(self):
        with self.assertRaises(ValueError):
            min_Swaps('01011', '1010')
