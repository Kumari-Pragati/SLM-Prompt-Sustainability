import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(is_num_decagonal(1), 0)
        self.assertEqual(is_num_decagonal(2), 4)
        self.assertEqual(is_num_decagonal(3), 15)
        self.assertEqual(is_num_decagonal(4), 36)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(is_num_decagonal(0), 0)
        self.assertEqual(is_num_decagonal(-1), -3)
        self.assertEqual(is_num_decagonal(100), 4000)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(is_num_decagonal(1000), 400000)
        self.assertEqual(is_num_decagonal(10000), 40000000)
