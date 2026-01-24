import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_find_max_val_positive(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)

    def test_find_max_val_negative(self):
        self.assertEqual(find_max_val(-10, 2, 0), 0)

    def test_find_max_val_zero(self):
        self.assertEqual(find_max_val(0, 2, 0), 0)

    def test_find_max_val_x_zero(self):
        self.assertEqual(find_max_val(10, 0, 0), -1)

    def test_find_max_val_y_zero(self):
        self.assertEqual(find_max_val(10, 2, 2), 10)

    def test_find_max_val_n_zero(self):
        self.assertEqual(find_max_val(0, 2, 0), -1)

    def test_find_max_val_x_negative(self):
        self.assertEqual(find_max_val(10, -2, 0), 0)

    def test_find_max_val_y_negative(self):
        self.assertEqual(find_max_val(10, 2, -2), 10)

    def test_find_max_val_n_negative(self):
        self.assertEqual(find_max_val(-10, 2, 0), -1)
