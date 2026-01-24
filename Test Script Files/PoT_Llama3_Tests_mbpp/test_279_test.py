import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(is_num_decagonal(0), 0)
        self.assertEqual(is_num_decagonal(1), 3)
        self.assertEqual(is_num_decagonal(2), 15)
        self.assertEqual(is_num_decagonal(3), 39)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(is_num_decagonal(-1), -3)
        self.assertEqual(is_num_decagonal(-2), -15)
        self.assertEqual(is_num_decagonal(0.5), 3.75)

    def test_corner_cases(self):
        self.assertEqual(is_num_decagonal(-0.5), -3.75)
        self.assertEqual(is_num_decagonal(1.5), 15.75)
