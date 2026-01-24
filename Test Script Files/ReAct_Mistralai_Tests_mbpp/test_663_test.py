import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_max_val(10, 2, 1), 10)
        self.assertEqual(find_max_val(5, 3, 0), 3)
        self.assertEqual(find_max_val(100, 7, 2), 102)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(find_max_val(-5, 2, 1), -1)
        self.assertEqual(find_max_val(0, 3, 2), -1)

    def test_x_is_zero(self):
        self.assertEqual(find_max_val(10, 0, 1), -1)

    def test_y_is_out_of_range(self):
        self.assertEqual(find_max_val(10, 2, 3), -1)
        self.assertEqual(find_max_val(10, 2, -3), -1)

    def test_n_is_zero(self):
        self.assertEqual(find_max_val(0, 2, 1), -1)

    def test_n_is_negative(self):
        self.assertEqual(find_max_val(-5, 2, 1), -1)
