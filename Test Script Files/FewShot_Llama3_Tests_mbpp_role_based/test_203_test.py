import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):
    def test_hamming_distance_of_two_numbers(self):
        self.assertEqual(hamming_Distance(5, 7), 2)

    def test_hamming_distance_of_zero_and_zero(self):
        self.assertEqual(hamming_Distance(0, 0), 0)

    def test_hamming_distance_of_positive_and_negative(self):
        self.assertEqual(hamming_Distance(5, -5), 2)

    def test_hamming_distance_of_large_numbers(self):
        self.assertEqual(hamming_Distance(1000, 1001), 1)

    def test_hamming_distance_of_binary_strings(self):
        self.assertEqual(hamming_Distance(0b1010, 0b1100), 2)
