import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_find_positive_numbers(self):
        self.assertEqual(find(10, 2), 5)
        self.assertEqual(find(15, 3), 5)
        self.assertEqual(find(20, 4), 5)

    def test_find_negative_numbers(self):
        self.assertEqual(find(-10, -2), 5)
        self.assertEqual(find(-15, -3), 5)
        self.assertEqual(find(-20, -4), 5)

    def test_find_mixed_numbers(self):
        self.assertEqual(find(-10, 2), -5)
        self.assertEqual(find(15, -3), -5)
        self.assertEqual(find(-20, 4), -5)

    def test_find_zero(self):
        self.assertEqual(find(0, 1), 0)
        self.assertEqual(find(0, -1), 0)

    def test_find_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)
