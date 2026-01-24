import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_hamming_distance_simple(self):
        self.assertEqual(hamming_Distance(6, 3), 3)
        self.assertEqual(hamming_Distance(5, 2), 3)
        self.assertEqual(hamming_Distance(1, 0), 1)

    def test_hamming_distance_edge_cases(self):
        self.assertEqual(hamming_Distance(0, 1), 1)
        self.assertEqual(hamming_Distance(1, 0), 1)
        self.assertEqual(hamming_Distance(0, 0), 0)

    def test_hamming_distance_complex(self):
        self.assertEqual(hamming_Distance(10, 2), 3)
        self.assertEqual(hamming_Distance(13, 10), 3)
        self.assertEqual(hamming_Distance(255, 254), 1)
