import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Total_Hamming_Distance(1), 1)
        self.assertEqual(Total_Hamming_Distance(2), 2)
        self.assertEqual(Total_Hamming_Distance(4), 4)
        self.assertEqual(Total_Hamming_Distance(8), 8)

    def test_edge_cases(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(10), 10)

    def test_boundary_cases(self):
        self.assertEqual(Total_Hamming_Distance(15), 15)
        self.assertEqual(Total_Hamming_Distance(31), 31)

    def test_corner_cases(self):
        self.assertEqual(Total_Hamming_Distance(32), 32)
        self.assertEqual(Total_Hamming_Distance(64), 64)
