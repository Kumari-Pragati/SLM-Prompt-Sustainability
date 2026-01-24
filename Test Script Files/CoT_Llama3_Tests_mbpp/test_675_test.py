import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_nums(1, 2, 5, 10), 3)

    def test_edge_case_in_range(self):
        self.assertEqual(sum_nums(8, 9, 5, 10), 20)

    def test_edge_case_out_of_range(self):
        self.assertEqual(sum_nums(1, 2, 5, 10), 3)

    def test_edge_case_equal_to_range(self):
        self.assertEqual(sum_nums(5, 5, 5, 10), 10)

    def test_edge_case_equal_to_range_reverse(self):
        self.assertEqual(sum_nums(10, 5, 5, 10), 15)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sum_nums('a', 2, 5, 10)

    def test_invalid_input_type_reverse(self):
        with self.assertRaises(TypeError):
            sum_nums(2, 'a', 5, 10)

    def test_invalid_input_type_range(self):
        with self.assertRaises(TypeError):
            sum_nums(2, 3, 'a', 10)

    def test_invalid_input_type_range_reverse(self):
        with self.assertRaises(TypeError):
            sum_nums(2, 3, 10, 'a')
