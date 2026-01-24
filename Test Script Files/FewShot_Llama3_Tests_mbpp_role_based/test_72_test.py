import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):
    def test_true_for_divisible_by_4(self):
        self.assertTrue(dif_Square(4))

    def test_true_for_divisible_by_4_with_negative_number(self):
        self.assertTrue(dif_Square(-4))

    def test_false_for_not_divisible_by_4(self):
        self.assertFalse(dif_Square(1))

    def test_false_for_not_divisible_by_4_with_negative_number(self):
        self.assertFalse(dif_Square(-1))

    def test_false_for_divisible_by_4_with_offset(self):
        self.assertFalse(dif_Square(8))
