import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)

    def test_edge_case_x_zero(self):
        self.assertEqual(find_max_val(10, 0, 0), 0)

    def test_edge_case_y_zero(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)

    def test_edge_case_n_zero(self):
        self.assertEqual(find_max_val(0, 2, 0), -1)

    def test_edge_case_x_one(self):
        self.assertEqual(find_max_val(10, 1, 0), 10)

    def test_edge_case_y_one(self):
        self.assertEqual(find_max_val(10, 2, 1), 1)

    def test_edge_case_n_one(self):
        self.assertEqual(find_max_val(1, 2, 0), 1)

    def test_edge_case_x_negative(self):
        self.assertEqual(find_max_val(10, -2, 0), -1)

    def test_edge_case_y_negative(self):
        self.assertEqual(find_max_val(10, 2, -1), -1)

    def test_edge_case_n_negative(self):
        self.assertEqual(find_max_val(-10, 2, 0), -1)

    def test_edge_case_x_zero_y_nonzero(self):
        self.assertEqual(find_max_val(10, 0, 1), -1)

    def test_edge_case_y_zero_x_nonzero(self):
        self.assertEqual(find_max_val(10, 1, 0), 10)

    def test_edge_case_n_zero_y_nonzero(self):
        self.assertEqual(find_max_val(0, 2, 1), -1)

    def test_edge_case_n_zero_x_nonzero(self):
        self.assertEqual(find_max_val(0, 1, 0), -1)

    def test_edge_case_n_zero_y_zero(self):
        self.assertEqual(find_max_val(0, 0, 0), -1)
