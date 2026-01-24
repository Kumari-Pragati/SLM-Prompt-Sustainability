import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(3), 1)
        self.assertEqual(Total_Hamming_Distance(6), 1)
        self.assertEqual(Total_Hamming_Distance(7), 1)
        self.assertEqual(Total_Hamming_Distance(10), 2)
        self.assertEqual(Total_Hamming_Distance(15), 3)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)
        self.assertEqual(Total_Hamming_Distance(4), 1)
        self.assertEqual(Total_Hamming_Distance(5), 2)
        self.assertEqual(Total_Hamming_Distance(8), 2)
        self.assertEqual(Total_Hamming_Distance(9), 2)
        self.assertEqual(Total_Hamming_Distance(16), 4)
        self.assertEqual(Total_Hamming_Distance(255), 128)
        self.assertEqual(Total_Hamming_Distance(256), 0)
        self.assertEqual(Total_Hamming_Distance(511), 256)
        self.assertEqual(Total_Hamming_Distance(1023), 512)
        self.assertEqual(Total_Hamming_Distance(1024), 0)
        self.assertEqual(Total_Hamming_Distance(1025), 512)
