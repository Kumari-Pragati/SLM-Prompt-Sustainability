import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 24)

    def test_edge_case(self):
        self.assertEqual(maximum_Sum([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    def test_boundary_case(self):
        self.assertEqual(maximum_Sum([[100000, 100000, 100000], [-100000, -100000, -100000]]), 300000)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -6)

    def test_single_list(self):
        self.assertEqual(maximum_Sum([[1, 2, 3]]), 6)

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), -100000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            maximum_Sum("not a list")
