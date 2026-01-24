import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_simple_case(self):
        self.assertListEqual(find_tuples([[10, 20], [30, 40], [50, 60]], 10), '[[10, 20], [50, 60]]')

    def test_edge_case_empty_list(self):
        self.assertEqual(find_tuples([], 3), '[]')

    def test_edge_case_single_element(self):
        self.assertEqual(find_tuples([[15]], 3), '[]')

    def test_edge_case_single_element_zero(self):
        self.assertEqual(find_tuples([[0]], 3), '[]')

    def test_edge_case_negative_numbers(self):
        self.assertEqual(find_tuples([[-10, 20], [-30, 40], [-50, 60]], 10), '[]')

    def test_edge_case_non_integer_numbers(self):
        self.assertEqual(find_tuples([[3.14, 2.71], [5, 4]], 1), '[]')

    def test_edge_case_floating_point_numbers(self):
        self.assertEqual(find_tuples([[3, 2.71], [5, 4]], 1), '[]')

    def test_complex_case_mixed_numbers(self):
        self.assertEqual(find_tuples([[10, 20], [30, 40], [50, 60.5], [70, 80]], 10), '[[10, 20], [50, 60.5]]')
