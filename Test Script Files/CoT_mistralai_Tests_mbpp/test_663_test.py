import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_max_val(10, 2, 1), 1)
        self.assertEqual(find_max_val(10, 3, 0), 9)
        self.assertEqual(find_max_val(10, 4, 3), 4)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(find_max_val(-5, 2, 1), -1)
        self.assertEqual(find_max_val(0, 2, 1), -1)

    def test_non_integer_input(self):
        self.assertRaises(TypeError, find_max_val, 10, 2.5, 1)
        self.assertRaises(TypeError, find_max_val, 10, 2, 'y')

    def test_negative_x(self):
        self.assertEqual(find_max_val(10, -2, 1), -1)

    def test_x_zero(self):
        self.assertEqual(find_max_val(10, 0, 1), -1)

    def test_y_out_of_range(self):
        self.assertEqual(find_max_val(10, 2, 2), -1)
        self.assertEqual(find_max_val(10, 2, 3), -1)
