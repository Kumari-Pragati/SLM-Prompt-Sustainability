import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(Total_Hamming_Distance(1), 1)
        self.assertEqual(Total_Hamming_Distance(2), 2)
        self.assertEqual(Total_Hamming_Distance(3), 4)
        self.assertEqual(Total_Hamming_Distance(4), 4)
        self.assertEqual(Total_Hamming_Distance(5), 6)
        self.assertEqual(Total_Hamming_Distance(6), 6)
        self.assertEqual(Total_Hamming_Distance(7), 8)
        self.assertEqual(Total_Hamming_Distance(8), 8)

    def test_edge_conditions(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(9), 12)
        self.assertEqual(Total_Hamming_Distance(10), 12)
        self.assertEqual(Total_Hamming_Distance(11), 14)
        self.assertEqual(Total_Hamming_Distance(12), 14)
        self.assertEqual(Total_Hamming_Distance(13), 16)
        self.assertEqual(Total_Hamming_Distance(14), 16)
        self.assertEqual(Total_Hamming_Distance(15), 18)
        self.assertEqual(Total_Hamming_Distance(16), 18)

    def test_complex_cases(self):
        self.assertEqual(Total_Hamming_Distance(17), 20)
        self.assertEqual(Total_Hamming_Distance(18), 20)
        self.assertEqual(Total_Hamming_Distance(19), 22)
        self.assertEqual(Total_Hamming_Distance(20), 22)
        self.assertEqual(Total_Hamming_Distance(21), 24)
        self.assertEqual(Total_Hamming_Distance(22), 24)
        self.assertEqual(Total_Hamming_Distance(23), 26)
        self.assertEqual(Total_Hamming_Distance(24), 26)
