import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_find_max_val_positive(self):
        self.assertEqual(find_max_val(5, 1, 2), 3)
        self.assertEqual(find_max_val(10, 2, 1), 5)
        self.assertEqual(find_max_val(15, 3, 2), 9)

    def test_find_max_val_zero(self):
        self.assertEqual(find_max_val(0, 1, 0), -1)

    def test_find_max_val_negative(self):
        self.assertEqual(find_max_val(-5, 1, 2), -1)
        self.assertEqual(find_max_val(-10, 2, 1), -1)
        self.assertEqual(find_max_val(-15, 3, 2), -1)

    def test_find_max_val_invalid_input(self):
        self.assertRaises(ValueError, find_max_val, -1, 2, 1)
        self.assertRaises(ValueError, find_max_val, 0, 0, 1)
        self.assertRaises(ValueError, find_max_val, 1, 0, 2)
