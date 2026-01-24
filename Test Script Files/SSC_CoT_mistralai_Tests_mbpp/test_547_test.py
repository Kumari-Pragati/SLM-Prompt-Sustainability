import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(Total_Hamming_Distance(10), 3)
        self.assertEqual(Total_Hamming_Distance(20), 5)
        self.assertEqual(Total_Hamming_Distance(40), 9)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)
        self.assertEqual(Total_Hamming_Distance(3), 1)
        self.assertEqual(Total_Hamming_Distance(4), 2)
        self.assertEqual(Total_Hamming_Distance(5), 2)
        self.assertEqual(Total_Hamming_Distance(6), 3)
        self.assertEqual(Total_Hamming_Distance(7), 3)
        self.assertEqual(Total_Hamming_Distance(8), 2)
        self.assertEqual(Total_Hamming_Distance(9), 3)
        self.assertEqual(Total_Hamming_Distance(16), 4)
        self.assertEqual(Total_Hamming_Distance(31), 5)
        self.assertEqual(Total_Hamming_Distance(63), 6)
        self.assertEqual(Total_Hamming_Distance(127), 6)
        self.assertEqual(Total_Hamming_Distance(255), 8)
        self.assertEqual(Total_Hamming_Distance(511), 8)
        self.assertEqual(Total_Hamming_Distance(1023), 8)
        self.assertEqual(Total_Hamming_Distance(2047), 8)
        self.assertEqual(Total_Hamming_Distance(4095), 10)
