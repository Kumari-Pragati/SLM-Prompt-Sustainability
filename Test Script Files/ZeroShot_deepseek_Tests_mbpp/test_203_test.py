import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(hamming_Distance(1, 4), 2)
        self.assertEqual(hamming_Distance(15, 10), 3)
        self.assertEqual(hamming_Distance(255, 128), 8)

    def test_zero(self):
        self.assertEqual(hamming_Distance(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(hamming_Distance(-1, -4), 3)
        self.assertEqual(hamming_Distance(-15, -10), 3)

    def test_large_numbers(self):
        self.assertEqual(hamming_Distance(1000000000, 2000000000), 19)
