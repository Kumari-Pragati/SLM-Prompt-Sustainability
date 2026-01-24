import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_max_val(10, 2, 1), 8)

    def test_edge_case_x_y_equal_to_1(self):
        self.assertEqual(find_max_val(10, 1, 1), 10)

    def test_edge_case_x_y_equal_to_n(self):
        self.assertEqual(find_max_val(10, 10, 0), 10)

    def test_edge_case_x_y_equal_to_0(self):
        self.assertEqual(find_max_val(10, 0, 0), 0)

    def test_edge_case_n_equal_to_0(self):
        self.assertEqual(find_max_val(0, 2, 1), -1)

    def test_edge_case_x_equal_to_0(self):
        self.assertEqual(find_max_val(10, 0, 1), -1)

    def test_edge_case_y_equal_to_0(self):
        self.assertEqual(find_max_val(10, 2, 0), -1)

    def test_edge_case_x_y_greater_than_n(self):
        self.assertEqual(find_max_val(10, 12, 1), -1)

    def test_edge_case_x_y_less_than_0(self):
        self.assertEqual(find_max_val(10, -2, 1), -1)
