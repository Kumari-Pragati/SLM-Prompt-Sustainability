import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((1+3+5), (2+4)))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(sum_of_alternates(()), ((0), (0)))

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(sum_of_alternates((1,)), ((1), (0)))

    def test_edge_case_two_element_tuple(self):
        self.assertEqual(sum_of_alternates((1, 2)), ((1), (2)))

    def test_edge_case_three_element_tuple(self):
        self.assertEqual(sum_of_alternates((1, 2, 3)), ((1+3), (2)))

    def test_edge_case_tuple_with_repeated_elements(self):
        self.assertEqual(sum_of_alternates((1, 1, 2, 2, 3, 3)), ((1+1+3+3), (2+2)))

    def test_edge_case_tuple_with_negative_elements(self):
        self.assertEqual(sum_of_alternates((-1, -2, -3, -4, -5)), ((-1-3-5), (-2-4)))

    def test_edge_case_tuple_with_mixed_positive_and_negative_elements(self):
        self.assertEqual(sum_of_alternates((1, -2, 3, -4, 5)), ((1+3+5), (-2-4)))
