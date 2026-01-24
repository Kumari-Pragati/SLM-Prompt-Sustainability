import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):

    def test_count_alpha_dig_spl(self):
        self.assertEqual(count_alpha_dig_spl("abc123"), (3, 3, 0))
        self.assertEqual(count_alpha_dig_spl("abc123@#$"), (3, 3, 3))
        self.assertEqual(count_alpha_dig_spl("123"), (0, 3, 0))
        self.assertEqual(count_alpha_dig_spl("@#$"), (0, 0, 3))
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))
