import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3), [2, 3, 4, 6, 8, 9])

    def test_edge_case_m_divisor(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 3), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_n_divisor(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 9), [2, 3, 4, 6, 8])

    def test_edge_case_no_divisor(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 8), [])

    def test_edge_case_single_number(self):
        self.assertEqual(div_of_nums([5], 2, 3), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(div_of_nums([], 2, 3), [])

    def test_invalid_input_m_zero(self):
        with self.assertRaises(TypeError):
            div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 3)

    def test_invalid_input_n_zero(self):
        with self.assertRaises(TypeError):
            div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 0)

    def test_invalid_input_negative_m(self):
        with self.assertRaises(TypeError):
            div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], -2, 3)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(TypeError):
            div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, -3)
