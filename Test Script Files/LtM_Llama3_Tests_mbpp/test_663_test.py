import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(find_max_val(10, 2, 0), 2)

    def test_edge_case_x_zero(self):
        self.assertEqual(find_max_val(10, 0, 0), 0)

    def test_edge_case_y_zero(self):
        self.assertEqual(find_max_val(10, 2, 0), 2)

    def test_edge_case_n_zero(self):
        self.assertEqual(find_max_val(0, 2, 0), -1)

    def test_edge_case_x_greater_than_n(self):
        self.assertEqual(find_max_val(10, 12, 0), -1)

    def test_edge_case_y_greater_than_n(self):
        self.assertEqual(find_max_val(10, 2, 12), -1)

    def test_edge_case_n_greater_than_x_y(self):
        self.assertEqual(find_max_val(12, 2, 0), 2)

    def test_edge_case_x_y_equal_n(self):
        self.assertEqual(find_max_val(10, 10, 0), 10)

    def test_edge_case_x_y_greater_than_n(self):
        self.assertEqual(find_max_val(10, 12, 12), -1)

    def test_edge_case_x_y_negative(self):
        self.assertEqual(find_max_val(10, -2, -2), -1)

    def test_edge_case_n_negative(self):
        self.assertEqual(find_max_val(-10, 2, 0), -1)

    def test_edge_case_x_y_negative(self):
        self.assertEqual(find_max_val(10, -2, -2), -1)
