import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_max_val(10, 2, 1), 2)

    def test_edge_case_x_equal_y(self):
        self.assertEqual(find_max_val(10, 2, 2), 2)

    def test_edge_case_x_divides_y(self):
        self.assertEqual(find_max_val(10, 5, 0), 0)

    def test_edge_case_n_equal_zero(self):
        self.assertEqual(find_max_val(0, 2, 1), -1)

    def test_edge_case_x_equal_n(self):
        self.assertEqual(find_max_val(10, 10, 0), 10)

    def test_edge_case_y_greater_than_x(self):
        self.assertEqual(find_max_val(10, 2, 3), 2)

    def test_edge_case_y_equal_zero(self):
        self.assertEqual(find_max_val(10, 2, 0), 0)

    def test_edge_case_x_equal_zero(self):
        self.assertEqual(find_max_val(10, 0, 1), -1)

    def test_edge_case_n_greater_than_x(self):
        self.assertEqual(find_max_val(20, 2, 1), 2)

    def test_edge_case_x_greater_than_n(self):
        self.assertEqual(find_max_val(10, 11, 1), -1)

    def test_edge_case_y_greater_than_n(self):
        self.assertEqual(find_max_val(10, 2, 12), -1)

    def test_edge_case_x_equal_y_equal_n(self):
        self.assertEqual(find_max_val(10, 10, 10), 10)

    def test_edge_case_x_equal_y_equal_zero(self):
        self.assertEqual(find_max_val(10, 0, 0), -1)
