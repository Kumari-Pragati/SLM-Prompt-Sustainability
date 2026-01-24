import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3), [2, 3, 4, 6, 8, 9])

    def test_edge_case_m_divides_all(self):
        self.assertEqual(div_of_nums([2, 4, 6, 8, 10], 2, 3), [2, 4, 6, 8, 10])

    def test_edge_case_n_divides_all(self):
        self.assertEqual(div_of_nums([3, 6, 9, 12, 15], 2, 3), [3, 6, 9, 12, 15])

    def test_edge_case_m_and_n_divides_all(self):
        self.assertEqual(div_of_nums([6, 12, 18, 24, 30], 2, 3), [6, 12, 18, 24, 30])

    def test_boundary_case_empty_list(self):
        self.assertEqual(div_of_nums([], 2, 3), [])

    def test_boundary_case_single_element(self):
        self.assertEqual(div_of_nums([1], 2, 3), [])

    def test_boundary_case_m_and_n_are_1(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 1, 1), [1, 2, 3, 4, 5])

    def test_special_case_m_and_n_are_same(self):
        self.assertEqual(div_of_nums([6, 12, 18, 24, 30], 2, 2), [6, 12, 18, 24, 30])

    def test_invalid_input_m_and_n_are_zero(self):
        with self.assertRaises(ValueError):
            div_of_nums([1, 2, 3, 4, 5], 0, 0)

    def test_invalid_input_negative_numbers(self):
        with self.assertRaises(ValueError):
            div_of_nums([1, 2, 3, 4, 5], -1, 2)
