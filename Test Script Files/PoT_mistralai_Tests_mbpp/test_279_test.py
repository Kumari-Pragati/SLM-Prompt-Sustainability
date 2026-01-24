import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(is_num_decagonal(1), 3)
        self.assertEqual(is_num_decagonal(2), 12)
        self.assertEqual(is_num_decagonal(3), 39)
        self.assertEqual(is_num_decagonal(4), 108)
        self.assertEqual(is_num_decagonal(5), 195)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(is_num_decagonal(0), -3)
        self.assertEqual(is_num_decagonal(10), 4030)
        self.assertEqual(is_num_decagonal(-1), -15)
        self.assertEqual(is_num_decagonal(20), 16803)
