import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):

    def test_find_positive_numbers(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(15, 3), 0)
        self.assertEqual(find(21, 3), 2)

    def test_find_zero(self):
        self.assertEqual(find(0, 3), 0)

    def test_find_negative_numbers(self):
        self.assertEqual(find(-10, 3), 1)
        self.assertEqual(find(-15, 3), 2)
        self.assertEqual(find(-21, 3), 0)

    def test_find_divisible_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find(0, 0)
