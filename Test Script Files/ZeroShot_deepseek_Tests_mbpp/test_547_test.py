import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(Total_Hamming_Distance(10), 12)
        self.assertEqual(Total_Hamming_Distance(20), 30)
        self.assertEqual(Total_Hamming_Distance(100), 240)

    def test_zero(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(Total_Hamming_Distance(-10), 0)
        self.assertEqual(Total_Hamming_Distance(-20), 0)
        self.assertEqual(Total_Hamming_Distance(-100), 0)

    def test_large_numbers(self):
        self.assertEqual(Total_Hamming_Distance(1000000000), 1000000000)
