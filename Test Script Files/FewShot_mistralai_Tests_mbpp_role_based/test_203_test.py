import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):
    def test_same_numbers(self):
        self.assertEqual(hamming_Distance(10, 10), 0)

    def test_single_bit_difference(self):
        self.assertEqual(hamming_Distance(5, 6), 1)

    def test_multiple_bit_differences(self):
        self.assertEqual(hamming_Distance(13, 15), 2)

    def test_zero(self):
        self.assertEqual(hamming_Distance(0, 0), 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, hamming_Distance, -1, -2)

    def test_non_integer_inputs(self):
        self.assertRaises(TypeError, hamming_Distance, 3.14, 2)
