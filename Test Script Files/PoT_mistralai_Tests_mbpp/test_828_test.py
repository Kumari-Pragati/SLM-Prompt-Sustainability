import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_alpha_dig_spl("Hello123World456!"), (7, 3, 4))

    def test_edge_case_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_edge_case_single_char(self):
        self.assertEqual(count_alpha_dig_spl("A"), (1, 0, 0))
        self.assertEqual(count_alpha_dig_spl("1"), (0, 1, 0))
        self.assertEqual(count_alpha_dig_spl("!"), (0, 0, 1))

    def test_boundary_case_long_string(self):
        long_string = "a" * 100 + "1" * 100 + "!" * 100
        self.assertEqual(count_alpha_dig_spl(long_string), (100, 100, 100))
