import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):
    def test_find_positive_numbers(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(21, 7), 4)
        self.assertEqual(find(100, 17), 10)

    def test_find_zero(self):
        self.assertEqual(find(0, 3), 0)

    def test_find_negative_numbers(self):
        self.assertEqual(find(-10, 3), 1)
        self.assertEqual(find(-21, 7), 4)
        self.assertEqual(find(-100, 17), 10)

    def test_find_divisible_by_zero(self):
        self.assertRaises(ZeroDivisionError, find, 10, 0)

    def test_find_non_integer_inputs(self):
        self.assertRaises(TypeError, find, 10.5, 3)
        self.assertRaises(TypeError, find, '10', 3)
