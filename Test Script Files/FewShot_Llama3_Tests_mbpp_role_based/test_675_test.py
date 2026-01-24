import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_nums(1, 2, 3, 5), 3)

    def test_edge_case_in_range(self):
        self.assertEqual(sum_nums(4, 5, 3, 6), 20)

    def test_edge_case_out_of_range(self):
        self.assertEqual(sum_nums(1, 2, 3, 5), 3)

    def test_edge_case_equal_to_range_start(self):
        self.assertEqual(sum_nums(3, 3, 3, 6), 6)

    def test_edge_case_equal_to_range_end(self):
        self.assertEqual(sum_nums(5, 5, 3, 6), 10)

    def test_edge_case_equal_to_range_start_and_end(self):
        self.assertEqual(sum_nums(3, 3, 3, 3), 6)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sum_nums("a", "b", 3, 5)
