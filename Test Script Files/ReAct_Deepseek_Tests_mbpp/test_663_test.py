import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)

    def test_edge_case_x_greater_than_n(self):
        self.assertEqual(find_max_val(5, 10, 0), -1)

    def test_edge_case_y_greater_than_n(self):
        self.assertEqual(find_max_val(5, 2, 7), -1)

    def test_edge_case_x_equals_y(self):
        self.assertEqual(find_max_val(10, 2, 2), 8)

    def test_edge_case_x_equals_0(self):
        self.assertEqual(find_max_val(10, 0, 1), -1)

    def test_edge_case_y_equals_0(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)

    def test_edge_case_n_equals_0(self):
        self.assertEqual(find_max_val(0, 2, 1), -1)

    def test_edge_case_negative_values(self):
        self.assertEqual(find_max_val(-10, 2, 1), -1)

    def test_edge_case_negative_x(self):
        self.assertEqual(find_max_val(10, -2, 1), -1)

    def test_edge_case_negative_y(self):
        self.assertEqual(find_max_val(10, 2, -1), -1)

    def test_edge_case_negative_n(self):
        self.assertEqual(find_max_val(-10, 2, 1), -1)
