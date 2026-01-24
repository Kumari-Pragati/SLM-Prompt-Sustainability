import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):
    def test_find_positive_integer_division(self):
        self.assertEqual(find(45, 9), 5)
        self.assertEqual(find(100, 25), 4)
        self.assertEqual(find(1000, 250), 4)

    def test_find_zero_division(self):
        self.assertEqual(find(0, 2), 0)
        self.assertEqual(find(10, 0), 0)

    def test_find_negative_integer_division(self):
        self.assertEqual(find(-45, 9), -5)
        self.assertEqual(find(-100, 25), -4)
        self.assertEqual(find(-1000, 250), -4)

    def test_find_non_integer_input(self):
        self.assertRaises(TypeError, find, 45.5, 9)
        self.assertRaises(TypeError, find, 45, 'm')

    def test_find_negative_number_input(self):
        self.assertRaises(ValueError, find, -1, 0)
