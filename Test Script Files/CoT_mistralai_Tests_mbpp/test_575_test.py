import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(count_no(2, 3, 1, 5), 3)
        self.assertEqual(count_no(3, 1, 1, 3), 1)
        self.assertEqual(count_no(5, 5, 1, 25), 25)

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, count_no, 0, 1, 1, 1)

    def test_negative(self):
        self.assertRaises(ValueError, count_no, -1, 1, 1, 1)

    def test_invalid_range(self):
        self.assertRaises(ValueError, count_no, 2, 1, 5, 4)
        self.assertRaises(ValueError, count_no, 2, 1, 1, 0)
