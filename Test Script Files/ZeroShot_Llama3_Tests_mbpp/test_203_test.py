import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_hamming_distance(self):
        self.assertEqual(hamming_Distance(1, 2), 1)
        self.assertEqual(hamming_Distance(3, 5), 2)
        self.assertEqual(hamming_Distance(10, 15), 2)
        self.assertEqual(hamming_Distance(0, 0), 0)
        self.assertEqual(hamming_Distance(1, 1), 0)
        self.assertEqual(hamming_Distance(2, 3), 1)
        self.assertEqual(hamming_Distance(5, 5), 0)
        self.assertEqual(hamming_Distance(10, 10), 0)
        self.assertEqual(hamming_Distance(15, 15), 0)
        self.assertEqual(hamming_Distance(20, 20), 0)
