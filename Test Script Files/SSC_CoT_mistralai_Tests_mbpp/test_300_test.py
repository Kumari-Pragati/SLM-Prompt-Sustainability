import unittest
from mbpp_300_code import count_binary_seq

class TestCountBinarySeq(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_binary_seq(2), 3)
        self.assertEqual(count_binary_seq(3), 5)
        self.assertEqual(count_binary_seq(4), 13)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_binary_seq(0), 1)
        self.assertEqual(count_binary_seq(1), 1)
        self.assertEqual(count_binary_seq(50), 665280)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            count_binary_seq(-1)
        with self.assertRaises(ValueError):
            count_binary_seq(float('nan'))
        with self.assertRaises(TypeError):
            count_binary_seq('string')
