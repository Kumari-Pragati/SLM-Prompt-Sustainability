import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(move_num("A1B2C3D4"), "A1BC2D3T4")

    def test_empty_string(self):
        self.assertEqual(move_num(""), "")

    def test_only_digits(self):
        self.assertEqual(move_num("12345"), "12345")

    def test_only_non_digits(self):
        self.assertEqual(move_num("ABCDEFG"), "ABCDEFG")

    def test_mixed_case(self):
        self.assertEqual(move_num("a1B2c3D4"), "a1B2c3D4")

    def test_leading_digits(self):
        self.assertEqual(move_num("1A2B3C4"), "1A2B3C4")

    def test_trailing_digits(self):
        self.assertEqual(move_num("A1B2C3D4"), "A1B2C3D4T")

    def test_multiple_digits(self):
        self.assertEqual(move_num("A12B23C34D45"), "A12B23C34D45T")
