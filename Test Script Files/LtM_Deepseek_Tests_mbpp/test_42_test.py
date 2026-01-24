import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(find_Sum([1, 2, 3, 2, 1], 5), 4)

    def test_edge_condition_empty_input(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_edge_condition_single_element(self):
        self.assertEqual(find_Sum([1], 1), 0)

    def test_boundary_condition_maximum_values(self):
        self.assertEqual(find_Sum([1000000, 1000000], 2), 2000000)

    def test_complex_input(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 10), 20)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Sum("1, 2, 3, 2, 1", 5)
