import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotal_Hamming_Distance(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)
        self.assertEqual(Total_Hamming_Distance(3), 2)
        self.assertEqual(Total_Hamming_Distance(4), 2)
        self.assertEqual(Total_Hamming_Distance(5), 4)
        self.assertEqual(Total_Hamming_Distance(6), 5)
        self.assertEqual(Total_Hamming_Distance(7), 5)
        self.assertEqual(Total_Hamming_Distance(8), 7)
        self.assertEqual(Total_Hamming_Distance(9), 7)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Total_Hamming_Distance(10), 9)
        self.assertEqual(Total_Hamming_Distance(11), 9)
        self.assertEqual(Total_Hamming_Distance(12), 9)
        self.assertEqual(Total_Hamming_Distance(13), 10)
        self.assertEqual(Total_Hamming_Distance(14), 10)
        self.assertEqual(Total_Hamming_Distance(15), 11)
        self.assertEqual(Total_Hamming_Distance(16), 12)
        self.assertEqual(Total_Hamming_Distance(17), 12)
        self.assertEqual(Total_Hamming_Distance(18), 13)

    def test_complex_and_corner_cases(self):
        self.assertEqual(Total_Hamming_Distance(19), 13)
        self.assertEqual(Total_Hamming_Distance(20), 14)
        self.assertEqual(Total_Hamming_Distance(21), 14)
        self.assertEqual(Total_Hamming_Distance(22), 15)
        self.assertEqual(Total_Hamming_Distance(23), 15)
        self.assertEqual(Total_Hamming_Distance(24), 16)
        self.assertEqual(Total_Hamming_Distance(25), 16)
