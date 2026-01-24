import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_Jumps(2, 3, 5), 1.5)

    def test_edge_case_d_zero(self):
        self.assertEqual(min_Jumps(2, 3, 0), 0)

    def test_edge_case_d_equal_a(self):
        self.assertEqual(min_Jumps(2, 3, 2), 1)

    def test_edge_case_d_equal_b(self):
        self.assertEqual(min_Jumps(2, 3, 3), 1)

    def test_edge_case_d_greater_than_b(self):
        self.assertEqual(min_Jumps(2, 3, 4), 1)

    def test_invalid_input_d_negative(self):
        with self.assertRaises(ValueError):
            min_Jumps(2, 3, -1)

    def test_invalid_input_a_negative(self):
        with self.assertRaises(ValueError):
            min_Jumps(-1, 3, 5)

    def test_invalid_input_b_negative(self):
        with self.assertRaises(ValueError):
            min_Jumps(2, -1, 5)
