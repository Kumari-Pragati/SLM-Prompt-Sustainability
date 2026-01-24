import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_alpha_dig_spl("Hello123!"), (5, 3, 1))

    def test_edge_case_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_edge_case_single_char(self):
        self.assertEqual(count_alpha_dig_spl("a"), (1, 0, 0))
        self.assertEqual(count_alpha_dig_spl("1"), (0, 1, 0))
        self.assertEqual(count_alpha_dig_spl("!"), (0, 0, 1))

    def test_edge_case_single_digit(self):
        self.assertEqual(count_alpha_dig_spl("1"), (0, 1, 0))

    def test_edge_case_single_alpha(self):
        self.assertEqual(count_alpha_dig_spl("a"), (1, 0, 0))

    def test_edge_case_single_special(self):
        self.assertEqual(count_alpha_dig_spl("!"), (0, 0, 1))

    def test_edge_case_multiple_types(self):
        self.assertEqual(count_alpha_dig_spl("Hello123!"), (5, 3, 1))
        self.assertEqual(count_alpha_dig_spl("abc123!"), (3, 3, 1))
        self.assertEqual(count_alpha_dig_spl("123abc!"), (3, 3, 1))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            count_alpha_dig_spl(123)
