import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_alpha_dig_spl("abc123"), (3, 3, 0))
        self.assertEqual(count_alpha_dig_spl("abc123!@#"), (3, 3, 3))

    def test_edge_conditions(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))
        self.assertEqual(count_alpha_dig_spl("123"), (0, 3, 0))
        self.assertEqual(count_alpha_dig_spl("abc"), (3, 0, 0))

    def test_boundary_conditions(self):
        self.assertEqual(count_alpha_dig_spl("a"*10000 + "1"*10000), (10000, 10000, 0))
        self.assertEqual(count_alpha_dig_spl("a"*10001 + "1"*10001), (10001, 10001, 0))

    def test_complex_cases(self):
        self.assertEqual(count_alpha_dig_spl("abc!@#123"), (3, 3, 3))
        self.assertEqual(count_alpha_dig_spl("123abc!@#"), (3, 3, 3))
        self.assertEqual(count_alpha_dig_spl("!@#123abc"), (3, 3, 3))
