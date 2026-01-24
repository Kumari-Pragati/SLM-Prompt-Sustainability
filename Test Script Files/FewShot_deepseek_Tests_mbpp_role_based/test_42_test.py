import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 2, 1], 5), 4)

    def test_edge_condition(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_boundary_condition(self):
        self.assertEqual(find_Sum([1, 1], 2), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Sum("1, 2, 3, 2, 1", 5)
