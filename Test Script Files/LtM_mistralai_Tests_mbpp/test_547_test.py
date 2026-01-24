import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)
        self.assertEqual(Total_Hamming_Distance(3), 1)
        self.assertEqual(Total_Hamming_Distance(4), 2)
        self.assertEqual(Total_Hamming_Distance(5), 2)
        self.assertEqual(Total_Hamming_Distance(6), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1023), 1022)
        self.assertEqual(Total_Hamming_Distance(1024), 1023)
        self.assertEqual(Total_Hamming_Distance(1025), 1024)
        self.assertEqual(Total_Hamming_Distance(2047), 2046)
        self.assertEqual(Total_Hamming_Distance(2048), 2047)
        self.assertEqual(Total_Hamming_Distance(2049), 2048)

    def test_complex_inputs(self):
        self.assertEqual(Total_Hamming_Distance(255), 254)
        self.assertEqual(Total_Hamming_Distance(256), 255)
        self.assertEqual(Total_Hamming_Distance(257), 256)
        self.assertEqual(Total_Hamming_Distance(258), 257)
        self.assertEqual(Total_Hamming_Distance(259), 258)
        self.assertEqual(Total_Hamming_Distance(16383), 16382)
        self.assertEqual(Total_Hamming_Distance(16384), 16383)
        self.assertEqual(Total_Hamming_Distance(16385), 16384)
