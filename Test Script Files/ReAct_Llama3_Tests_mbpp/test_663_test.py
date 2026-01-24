import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_max_val(10, 2, 1), 10)

    def test_edge_case_x_y_equal(self):
        self.assertEqual(find_max_val(10, 2, 0), 2)

    def test_edge_case_x_y_divisible(self):
        self.assertEqual(find_max_val(10, 3, 0), 9)

    def test_edge_case_x_y_not_divisible(self):
        self.assertEqual(find_max_val(10, 3, 1), 10)

    def test_edge_case_x_y_negative(self):
        self.assertEqual(find_max_val(10, -2, 1), -1)

    def test_edge_case_n_zero(self):
        self.assertEqual(find_max_val(0, 2, 1), -1)

    def test_edge_case_n_negative(self):
        self.assertEqual(find_max_val(-5, 2, 1), -1)

    def test_edge_case_x_zero(self):
        self.assertEqual(find_max_val(10, 0, 1), 10)

    def test_edge_case_y_zero(self):
        self.assertEqual(find_max_val(10, 2, 0), 2)

    def test_edge_case_x_y_negative(self):
        self.assertEqual(find_max_val(10, -2, -1), -1)

    def test_edge_case_x_y_divisible_negative(self):
        self.assertEqual(find_max_val(10, -3, 0), -1)

    def test_edge_case_x_y_not_divisible_negative(self):
        self.assertEqual(find_max_val(10, -3, 1), 10)
