import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps('0101', '1010'), 1)

    def test_typical_case_with_multiple_swaps(self):
        self.assertEqual(min_Swaps('010101', '101010'), 2)

    def test_boundary_case_with_empty_strings(self):
        self.assertEqual(min_Swaps('', ''), 0)

    def test_edge_case_with_same_strings(self):
        self.assertEqual(min_Swaps('0000', '0000'), 0)

    def test_edge_case_with_strings_of_same_characters(self):
        self.assertEqual(min_Swaps('0000', '1111'), -1)

    def test_edge_case_with_strings_of_different_lengths(self):
        self.assertEqual(min_Swaps('01010', '1010'), -1)

    def test_invalid_input_with_non_string_arguments(self):
        with self.assertRaises(TypeError):
            min_Swaps(1234, '1010')

        with self.assertRaises(TypeError):
            min_Swaps('0101', 1234)

        with self.assertRaises(TypeError):
            min_Swaps(1234, 1234)
