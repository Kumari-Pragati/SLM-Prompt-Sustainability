import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)
        self.assertEqual(find_max_val(10, 3, 1), 3)
        self.assertEqual(find_max_val(10, 4, 2), 8)

    def test_edge_case_x_zero(self):
        self.assertEqual(find_max_val(10, 0, 0), 0)

    def test_edge_case_y_out_of_range(self):
        self.assertEqual(find_max_val(10, 2, 5), -1)

    def test_edge_case_n_zero(self):
        self.assertEqual(find_max_val(0, 2, 0), -1)

    def test_corner_case_x_y_equal(self):
        self.assertEqual(find_max_val(10, 2, 2), 2)
