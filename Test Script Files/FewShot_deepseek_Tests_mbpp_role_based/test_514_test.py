import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_elements((1, 2, 3, 4, 5)), 15)

    def test_edge_condition(self):
        self.assertEqual(sum_elements(()), 0)

    def test_boundary_condition(self):
        self.assertEqual(sum_elements((1000,)), 1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_elements(123)
