import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(Total_Hamming_Distance(1), 1)
        self.assertEqual(Total_Hamming_Distance(2), 2)
        self.assertEqual(Total_Hamming_Distance(4), 4)
        self.assertEqual(Total_Hamming_Distance(8), 8)
        self.assertEqual(Total_Hamming_Distance(16), 16)
        self.assertEqual(Total_Hamming_Distance(32), 32)
        self.assertEqual(Total_Hamming_Distance(64), 64)
        self.assertEqual(Total_Hamming_Distance(128), 128)
        self.assertEqual(Total_Hamming_Distance(256), 256)
        self.assertEqual(Total_Hamming_Distance(512), 512)
        self.assertEqual(Total_Hamming_Distance(1024), 1024)

    def test_edge_cases(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1025), 1025)
        self.assertEqual(Total_Hamming_Distance(2048), 2048)
        self.assertEqual(Total_Hamming_Distance(4096), 4096)
        self.assertEqual(Total_Hamming_Distance(8192), 8192)
        self.assertEqual(Total_Hamming_Distance(16384), 16384)
        self.assertEqual(Total_Hamming_Distance(32768), 32768)
        self.assertEqual(Total_Hamming_Distance(65536), 65536)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Total_Hamming_Distance('1000')
        with self.assertRaises(TypeError):
            Total_Hamming_Distance(None)
        with self.assertRaises(TypeError):
            Total_Hamming_Distance([])
        with self.assertRaises(TypeError):
            Total_Hamming_Distance({})
