import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Jumps(1, 2, 3), 1.5)

    def test_edge_case_d_zero(self):
        self.assertEqual(min_Jumps(1, 2, 0), 0)

    def test_edge_case_d_a(self):
        self.assertEqual(min_Jumps(1, 2, 1), 1)

    def test_edge_case_d_b(self):
        self.assertEqual(min_Jumps(1, 2, 2), 2)

    def test_edge_case_d_greater_than_b(self):
        self.assertEqual(min_Jumps(1, 2, 3), 2)

    def test_invalid_input_d_negative(self):
        with self.assertRaises(ValueError):
            min_Jumps(1, 2, -1)

    def test_invalid_input_d_non_integer(self):
        with self.assertRaises(TypeError):
            min_Jumps(1, 2, 3.5)
