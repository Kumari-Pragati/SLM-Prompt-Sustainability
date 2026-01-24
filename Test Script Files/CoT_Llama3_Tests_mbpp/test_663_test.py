import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_max_val(10, 2, 1), 2)

    def test_edge_case_n_zero(self):
        self.assertEqual(find_max_val(0, 2, 1), -1)

    def test_edge_case_x_zero(self):
        self.assertEqual(find_max_val(10, 0, 1), -1)

    def test_edge_case_y_zero(self):
        self.assertEqual(find_max_val(10, 2, 0), 0)

    def test_edge_case_n_and_x_zero(self):
        self.assertEqual(find_max_val(0, 0, 1), -1)

    def test_edge_case_y_greater_than_x(self):
        self.assertEqual(find_max_val(10, 2, 3), -1)

    def test_edge_case_y_greater_than_n(self):
        self.assertEqual(find_max_val(10, 2, 12), -1)

    def test_edge_case_y_equal_to_n(self):
        self.assertEqual(find_max_val(10, 2, 10), 10)

    def test_edge_case_y_equal_to_zero(self):
        self.assertEqual(find_max_val(10, 2, 0), 0)

    def test_edge_case_x_greater_than_n(self):
        self.assertEqual(find_max_val(10, 15, 1), -1)

    def test_edge_case_x_greater_than_y(self):
        self.assertEqual(find_max_val(10, 3, 2), -1)

    def test_edge_case_y_greater_than_x_and_n(self):
        self.assertEqual(find_max_val(10, 5, 12), -1)
