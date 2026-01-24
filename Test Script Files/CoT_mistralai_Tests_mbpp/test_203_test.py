import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(hamming_Distance(0, 0), 0)

    def test_single_bit_difference(self):
        self.assertEqual(hamming_Distance(1, 2), 1)
        self.assertEqual(hamming_Distance(2, 3), 1)
        self.assertEqual(hamming_Distance(4, 5), 1)

    def test_multiple_bit_differences(self):
        self.assertEqual(hamming_Distance(3, 5), 2)
        self.assertEqual(hamming_Distance(7, 11), 3)
        self.assertEqual(hamming_Distance(15, 23), 4)

    def test_all_bits_different(self):
        self.assertEqual(hamming_Distance(1, 15), 4)
        self.assertEqual(hamming_Distance(13, 14), 1)

    def test_negative_numbers(self):
        self.assertRaises(TypeError, hamming_Distance, -1, -2)

    def test_floats(self):
        self.assertRaises(TypeError, hamming_Distance, 1.5, 2.5)

    def test_strings(self):
        self.assertRaises(TypeError, hamming_Distance, '1', '2')
