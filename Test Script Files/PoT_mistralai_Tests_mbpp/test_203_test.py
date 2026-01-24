import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(hamming_Distance(12, 10), 2)
        self.assertEqual(hamming_Distance(255, 128), 1)
        self.assertEqual(hamming_Distance(10101010, 10010101), 4)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(hamming_Distance(0, 1), 1)
        self.assertEqual(hamming_Distance(1, 0), 1)
        self.assertEqual(hamming_Distance(1, 1), 0)
        self.assertEqual(hamming_Distance(2 ** 31 - 1, 2 ** 31), 1)
        self.assertEqual(hamming_Distance(2 ** 31, 2 ** 31 - 1), 1)
