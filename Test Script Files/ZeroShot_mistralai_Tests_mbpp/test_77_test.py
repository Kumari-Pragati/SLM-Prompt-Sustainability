import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):

    def test_zero(self):
        self.assertFalse(is_Diff(0))

    def test_eleven(self):
        self.assertTrue(is_Diff(11))

    def test_twenty_two(self):
        self.assertFalse(is_Diff(22))

    def test_thirty_three(self):
        self.assertTrue(is_Diff(33))

    def test_sixty_six(self):
        self.assertFalse(is_Diff(66))

    def test_seventy_seven(self):
        self.assertTrue(is_Diff(77))

    def test_hundred(self):
        self.assertFalse(is_Diff(100))

    def test_negative_one(self):
        self.assertFalse(is_Diff(-1))

    def test_large_number(self):
        self.assertTrue(is_Diff(10000011))
