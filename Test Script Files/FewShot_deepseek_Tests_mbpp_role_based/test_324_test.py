import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((9), (5)))

    def test_edge_condition(self):
        self.assertEqual(sum_of_alternates(()), ((0), (0)))

    def test_boundary_condition(self):
        self.assertEqual(sum_of_alternates((1,)), ((1), (0)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_of_alternates(123)
