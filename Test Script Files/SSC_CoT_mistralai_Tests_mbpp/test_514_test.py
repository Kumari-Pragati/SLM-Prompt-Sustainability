import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)
        self.assertEqual(sum_elements((0, 0, 0)), 0)
        self.assertEqual(sum_elements((4, 9, 2)), 15)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_elements(()), 0)
        self.assertEqual(sum_elements((1,)), 1)
        self.assertEqual(sum_elements((1, 2, 3, 4, 5, 6, 7, 8, 9)), 45)

    def test_negative_numbers(self):
        self.assertEqual(sum_elements((-1, -2, -3)), -6)
        self.assertEqual(sum_elements((0, -1, 0)), -1)
        self.assertEqual(sum_elements((-4, -9, -2)), -15)

    def test_mixed_numbers(self):
        self.assertEqual(sum_elements((1, -2, 3)), 2)
        self.assertEqual(sum_elements((-1, 0, -1)), -2)
        self.assertEqual(sum_elements((1, -2, 3, -4, 5)), 4)
