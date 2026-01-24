import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)
        self.assertEqual(find_max_val(10, 3, 0), -1)
        self.assertEqual(find_max_val(10, 2, 1), 2)
        self.assertEqual(find_max_val(10, 2, 2), 4)

    def test_zero(self):
        self.assertEqual(find_max_val(0, 2, 0), 0)
        self.assertEqual(find_max_val(0, 3, 0), -1)

    def test_negative_numbers(self):
        self.assertEqual(find_max_val(-10, 2, 0), -10)
        self.assertEqual(find_max_val(-10, 3, 0), -1)
        self.assertEqual(find_max_val(-10, 2, 1), -10)
        self.assertEqual(find_max_val(-10, 2, -1), -2)
