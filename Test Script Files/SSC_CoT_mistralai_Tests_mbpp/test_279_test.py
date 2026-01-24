import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(is_num_decagonal(1), 3)
        self.assertEqual(is_num_decagonal(2), 12)
        self.assertEqual(is_num_decagonal(3), 39)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(is_num_decagonal(0), -3)
        self.assertEqual(is_num_decagonal(1000), 4000003)
        self.assertEqual(is_num_decagonal(-1), -15)

    def test_invalid_input(self):
        self.assertRaises(TypeError, is_num_decagonal, 'not_a_number')
