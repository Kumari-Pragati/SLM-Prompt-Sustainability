import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_alpha_dig_spl("HelloWorld123!"), (7, 3, 2))
        self.assertEqual(count_alpha_dig_spl("1234567890"), (0, 10, 0))
        self.assertEqual(count_alpha_dig_spl("AaBbCcDdEeFf"), (6, 0, 0))
        self.assertEqual(count_alpha_dig_spl("Ab1c2D3e4F5"), (4, 2, 1))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))
        self.assertEqual(count_alpha_dig_spl("A"), (1, 0, 0))
        self.assertEqual(count_alpha_dig_spl("1"), (0, 1, 0))
        self.assertEqual(count_alpha_dig_spl("!@#$%^&*()"), (0, 0, 7))
        self.assertEqual(count_alpha_dig_spl("0123456789"), (0, 10, 0))
        self.assertEqual(count_alpha_dig_spl("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), (26, 0, 0))
        self.assertEqual(count_alpha_dig_spl("abcdefghijklmnopqrstuvwxyz"), (26, 0, 0))
