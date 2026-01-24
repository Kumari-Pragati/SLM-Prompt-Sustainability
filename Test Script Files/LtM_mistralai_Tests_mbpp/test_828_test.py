import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(count_alpha_dig_spl("abc123!@#"), (3, 3, 1))

    def test_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_single_char_string(self):
        self.assertEqual(count_alpha_dig_spl("a"), (1, 0, 0))
        self.assertEqual(count_alpha_dig_spl("1"), (0, 1, 0))
        self.assertEqual(count_alpha_dig_spl("!"), (0, 0, 1))

    def test_min_max_length(self):
        self.assertEqual(count_alpha_dig_spl("a" * 100), (100, 0, 0))
        self.assertEqual(count_alpha_dig_spl("1" * 100), (0, 100, 0))
        self.assertEqual(count_alpha_dig_spl("!" * 100), (0, 0, 100))

    def test_mixed_string(self):
        self.assertEqual(count_alpha_dig_spl("a1b2c3!@#"), (3, 3, 1))

    def test_special_characters(self):
        self.assertEqual(count_alpha_dig_spl("a!b@c#"), (2, 0, 1))
        self.assertEqual(count_alpha_dig_spl("a$b%c^"), (2, 0, 1))
        self.assertEqual(count_alpha_dig_spl("a_b~c|"), (2, 0, 1))
