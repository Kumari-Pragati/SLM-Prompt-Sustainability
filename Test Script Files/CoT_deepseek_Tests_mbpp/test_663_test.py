import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)

    def test_edge_case_x_greater_than_n(self):
        self.assertEqual(find_max_val(5, 10, 0), -1)

    def test_edge_case_y_greater_than_n(self):
        self.assertEqual(find_max_val(5, 1, 6), -1)

    def test_edge_case_x_equals_y(self):
        self.assertEqual(find_max_val(10, 2, 2), 2)

    def test_edge_case_x_equals_1(self):
        self.assertEqual(find_max_val(10, 1, 0), 10)

    def test_edge_case_n_equals_0(self):
        self.assertEqual(find_max_val(0, 2, 1), -1)

    def test_edge_case_n_equals_1(self):
        self.assertEqual(find_max_val(1, 2, 1), -1)

    def test_edge_case_negative_n(self):
        self.assertEqual(find_max_val(-5, 2, 1), -1)

    def test_edge_case_negative_x(self):
        self.assertEqual(find_max_val(5, -2, 1), -1)

    def test_edge_case_negative_y(self):
        self.assertEqual(find_max_val(5, 2, -1), -1)

    def test_edge_case_negative_n_and_x(self):
        self.assertEqual(find_max_val(-5, -2, 1), -1)

    def test_edge_case_negative_n_and_y(self):
        self.assertEqual(find_max_val(-5, 2, -1), -1)

    def test_edge_case_negative_x_and_y(self):
        self.assertEqual(find_max_val(5, -2, -1), -1)

    def test_edge_case_negative_n_x_and_y(self):
        self.assertEqual(find_max_val(-5, -2, -1), -1)
