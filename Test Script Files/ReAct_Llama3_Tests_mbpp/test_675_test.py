import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_nums(5, 7, 10, 20), 12)

    def test_edge_case_in_range(self):
        self.assertEqual(sum_nums(15, 17, 10, 20), 20)

    def test_edge_case_out_of_range(self):
        self.assertEqual(sum_nums(5, 7, 20, 30), 12)

    def test_edge_case_equal_to_range_start(self):
        self.assertEqual(sum_nums(10, 10, 10, 20), 20)

    def test_edge_case_equal_to_range_end(self):
        self.assertEqual(sum_nums(19, 1, 10, 20), 20)

    def test_edge_case_equal_to_range_start_and_end(self):
        self.assertEqual(sum_nums(10, 10, 10, 10), 20)

    def test_edge_case_out_of_range_negative(self):
        self.assertEqual(sum_nums(-5, 7, -10, 20), 2)

    def test_edge_case_out_of_range_negative_equal_to_range_start(self):
        self.assertEqual(sum_nums(-10, 10, -10, 20), 20)

    def test_edge_case_out_of_range_negative_equal_to_range_end(self):
        self.assertEqual(sum_nums(-20, 1, -10, 20), 20)
