import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_find_positive_integer_division(self):
        self.assertEqual(find(18, 3), 6)
        self.assertEqual(find(45, 9), 5)
        self.assertEqual(find(100, 25), 4)

    def test_find_zero_division(self):
        self.assertEqual(find(10, 0), 0)

    def test_find_negative_integer_division(self):
        self.assertEqual(find(-18, 3), -6)
        self.assertEqual(find(-45, 9), -5)
        self.assertEqual(find(-100, 25), -4)

    def test_find_floor_division_with_remainder(self):
        self.assertEqual(find(17, 3), 5)
        self.assertEqual(find(47, 9), 5)
        self.assertEqual(find(99, 25), 4)

    def test_find_floor_division_with_negative_remainder(self):
        self.assertEqual(find(-17, 3), -6)
        self.assertEqual(find(-47, 9), -6)
        self.assertEqual(find(-99, 25), -4)
