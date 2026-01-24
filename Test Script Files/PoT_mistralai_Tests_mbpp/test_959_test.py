import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Average([1, 2, 3, 4, 5]), 3.0)

    def test_edge_case_empty_list(self):
        self.assertEqual(Average([]), 0.0)

    def test_edge_case_single_element(self):
        self.assertEqual(Average([1]), 1.0)

    def test_boundary_case_zero(self):
        self.assertEqual(Average([0]), 0.0)

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(Average([-1, -2, -3]), -2.0)
