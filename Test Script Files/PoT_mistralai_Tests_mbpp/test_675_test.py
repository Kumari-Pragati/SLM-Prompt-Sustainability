import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_nums(5, 3, 10, 20), 20)
        self.assertEqual(sum_nums(10, 5, 20, 30), 15)

    def test_edge_case_min(self):
        self.assertEqual(sum_nums(2, 3, 0, 4), None)

    def test_edge_case_max(self):
        self.assertEqual(sum_nums(2, 3, 50, 51), 20)

    def test_boundary_case_min(self):
        self.assertEqual(sum_nums(0, 3, 0, 4), None)

    def test_boundary_case_max(self):
        self.assertEqual(sum_nums(5, 3, 50, 50), 8)

    def test_invalid_input_x(self):
        self.assertRaises(TypeError, sum_nums, 'a', 3, 5, 10)

    def test_invalid_input_y(self):
        self.assertRaises(TypeError, sum_nums, 5, 'a', 5, 10)
