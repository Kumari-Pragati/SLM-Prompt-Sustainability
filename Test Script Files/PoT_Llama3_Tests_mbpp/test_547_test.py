import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotal_Hamming_Distance(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)
        self.assertEqual(Total_Hamming_Distance(3), 2)
        self.assertEqual(Total_Hamming_Distance(4), 2)
        self.assertEqual(Total_Hamming_Distance(5), 4)
        self.assertEqual(Total_Hamming_Distance(6), 5)
        self.assertEqual(Total_Hamming_Distance(7), 5)
        self.assertEqual(Total_Hamming_Distance(8), 7)
        self.assertEqual(Total_Hamming_Distance(9), 9)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(Total_Hamming_Distance(10), 9)
        self.assertEqual(Total_Hamming_Distance(11), 10)
        self.assertEqual(Total_Hamming_Distance(12), 11)
        self.assertEqual(Total_Hamming_Distance(13), 12)
        self.assertEqual(Total_Hamming_Distance(14), 13)
        self.assertEqual(Total_Hamming_Distance(15), 14)
        self.assertEqual(Total_Hamming_Distance(16), 15)
        self.assertEqual(Total_Hamming_Distance(17), 16)
        self.assertEqual(Total_Hamming_Distance(18), 17)
        self.assertEqual(Total_Hamming_Distance(19), 18)

    def test_corner_cases(self):
        self.assertEqual(Total_Hamming_Distance(20), 19)
        self.assertEqual(Total_Hamming_Distance(21), 20)
        self.assertEqual(Total_Hamming_Distance(22), 21)
        self.assertEqual(Total_Hamming_Distance(23), 22)
        self.assertEqual(Total_Hamming_Distance(24), 23)
        self.assertEqual(Total_Hamming_Distance(25), 24)
        self.assertEqual(Total_Hamming_Distance(26), 25)
        self.assertEqual(Total_Hamming_Distance(27), 26)
        self.assertEqual(Total_Hamming_Distance(28), 27)
        self.assertEqual(Total_Hamming_Distance(29), 28)
