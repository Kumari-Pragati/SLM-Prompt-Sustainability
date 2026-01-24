import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_simple_sum(self):
        self.assertEqual(sum_nums(1, 2, 3, 5), 3)
    def test_sum_in_range(self):
        self.assertEqual(sum_nums(4, 6, 3, 10), 20)
    def test_sum_out_of_range(self):
        self.assertEqual(sum_nums(1, 2, 3, 5), 3)
    def test_edge_case_m_equal_n(self):
        self.assertEqual(sum_nums(3, 3, 3, 3), 6)
    def test_edge_case_m_greater_n(self):
        self.assertEqual(sum_nums(3, 3, 10, 5), 6)
    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sum_nums('a', 2, 3, 5)
