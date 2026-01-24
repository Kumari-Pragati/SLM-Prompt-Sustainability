import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(hamming_Distance(6, 3), 3)
        self.assertEqual(hamming_Distance(10, 2), 4)
        self.assertEqual(hamming_Distance(1, 0), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(hamming_Distance(0, 1), 1)
        self.assertEqual(hamming_Distance(1, 0), 1)
        self.assertEqual(hamming_Distance(1, 1), 0)
        self.assertEqual(hamming_Distance(2 ** 31 - 1, 2 ** 31), 1)
        self.assertEqual(hamming_Distance(2 ** 31, 0), 32)

    def test_complex_inputs(self):
        self.assertEqual(hamming_Distance(13, 17), 4)
        self.assertEqual(hamming_Distance(11111111, 10111111), 7)
        self.assertEqual(hamming_Distance(1010101010, 0101010101), 16)
