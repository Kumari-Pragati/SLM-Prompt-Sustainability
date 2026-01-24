import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):

    def test_zero_distance(self):
        self.assertEqual(hamming_Distance(0, 0), 0)

    def test_identical_numbers(self):
        self.assertEqual(hamming_Distance(10, 10), 0)

    def test_single_bit_difference(self):
        self.assertEqual(hamming_Distance(1, 2), 1)
        self.assertEqual(hamming_Distance(3, 4), 1)
        self.assertEqual(hamming_Distance(5, 6), 1)

    def test_multiple_bit_differences(self):
        self.assertEqual(hamming_Distance(1, 3), 2)
        self.assertEqual(hamming_Distance(7, 11), 3)
        self.assertEqual(hamming_Distance(17, 23), 4)

    def test_negative_numbers(self):
        self.assertEqual(hamming_Distance(-1, -2), 1)
        self.assertEqual(hamming_Distance(-5, -3), 2)

    def test_one_number_is_zero(self):
        self.assertEqual(hamming_Distance(0, 1), 1)
        self.assertEqual(hamming_Distance(1, 0), 1)

    def test_large_numbers(self):
        self.assertEqual(hamming_Distance(2**16 - 1, 2**16 + 1), 1)
        self.assertEqual(hamming_Distance(2**32 - 1, 2**32 + 1), 1)
