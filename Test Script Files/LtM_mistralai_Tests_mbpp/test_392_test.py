import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_max_sum(1), 1)
        self.assertEqual(get_max_sum(2), 2)
        self.assertEqual(get_max_sum(3), 3)
        self.assertEqual(get_max_sum(4), 4)
        self.assertEqual(get_max_sum(5), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_max_sum(0), 0)
        self.assertEqual(get_max_sum(6), 6)
        self.assertEqual(get_max_sum(7), 7)
        self.assertEqual(get_max_sum(8), 8)
        self.assertEqual(get_max_sum(9), 9)

    def test_complex_inputs(self):
        self.assertEqual(get_max_sum(10), 20)
        self.assertEqual(get_max_sum(13), 23)
        self.assertEqual(get_max_sum(21), 57)
        self.assertEqual(get_max_sum(34), 105)
