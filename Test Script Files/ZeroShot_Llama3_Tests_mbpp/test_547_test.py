import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_total_hamming_distance(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)
        self.assertEqual(Total_Hamming_Distance(3), 2)
        self.assertEqual(Total_Hamming_Distance(4), 2)
        self.assertEqual(Total_Hamming_Distance(5), 4)
        self.assertEqual(Total_Hamming_Distance(6), 4)
        self.assertEqual(Total_Hamming_Distance(7), 4)
        self.assertEqual(Total_Hamming_Distance(8), 5)
        self.assertEqual(Total_Hamming_Distance(9), 5)
