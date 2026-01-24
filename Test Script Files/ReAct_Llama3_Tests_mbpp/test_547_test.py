import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)

    def test_single_bit(self):
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)

    def test_multiple_bits(self):
        self.assertEqual(Total_Hamming_Distance(3), 2)
        self.assertEqual(Total_Hamming_Distance(4), 2)
        self.assertEqual(Total_Hamming_Distance(5), 4)

    def test_large_numbers(self):
        self.assertEqual(Total_Hamming_Distance(10), 9)
        self.assertEqual(Total_Hamming_Distance(20), 19)
