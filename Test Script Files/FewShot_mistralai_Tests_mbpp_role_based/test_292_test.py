import unittest
from mbpp_292_code import find

class TestFind(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find(10, 2), 5)
        self.assertEqual(find(20, 4), 5)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            find(0, 2)

    def test_negative_numbers(self):
        self.assertEqual(find(-10, 2), -6)
        self.assertEqual(find(-20, 4), -5)

    def test_one(self):
        self.assertEqual(find(1, 1), 1)
