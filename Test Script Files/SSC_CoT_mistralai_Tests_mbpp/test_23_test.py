import unittest
from mbpp_23_code import maximum_Sum

class TestMaximumSum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(maximum_Sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)
        self.assertEqual(maximum_Sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), 36)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(maximum_Sum([[]]), 0)
        self.assertEqual(maximum_Sum([[0]]), 0)
        self.assertEqual(maximum_Sum([[100000]]), 100000)
        self.assertEqual(maximum_Sum([[-100000]]), -100000)
        self.assertEqual(maximum_Sum([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]), 34)

    def test_negative_numbers(self):
        self.assertEqual(maximum_Sum([[-1, -2, 3], [-4, 5, -6], [-7, 8, -9]]), 11)

    def test_empty_list(self):
        self.assertEqual(maximum_Sum([]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            maximum_Sum(123)
        with self.assertRaises(TypeError):
            maximum_Sum('abc')
