import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_find_divisor_equal(self):
        self.assertEqual(find_Divisor(4, 4), 4)

    def test_find_divisor_same_number(self):
        self.assertEqual(find_Divisor(5, 5), 5)

    def test_find_divisor_not_equal(self):
        self.assertEqual(find_Divisor(6, 4), 2)

    def test_find_divisor_zero(self):
        self.assertEqual(find_Divisor(0, 4), 2)

    def test_find_divisor_negative(self):
        self.assertEqual(find_Divisor(-6, 4), 2)
