import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(zigzag(3, 2), 2)

    def test_edge_case_n_zero(self):
        self.assertEqual(zigzag(0, 2), 1)

    def test_edge_case_k_zero(self):
        self.assertEqual(zigzag(3, 0), 0)

    def test_edge_case_n_and_k_zero(self):
        self.assertEqual(zigzag(0, 0), 1)

    def test_edge_case_n_negative(self):
        with self.assertRaises(TypeError):
            zigzag(-3, 2)

    def test_edge_case_k_negative(self):
        with self.assertRaises(TypeError):
            zigzag(3, -2)

    def test_edge_case_n_and_k_negative(self):
        with self.assertRaises(TypeError):
            zigzag(-3, -2)
