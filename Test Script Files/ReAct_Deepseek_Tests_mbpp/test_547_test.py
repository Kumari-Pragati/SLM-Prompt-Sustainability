import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Total_Hamming_Distance(1), 1)
        self.assertEqual(Total_Hamming_Distance(2), 2)
        self.assertEqual(Total_Hamming_Distance(4), 4)
        self.assertEqual(Total_Hamming_Distance(8), 8)

    def test_boundary_cases(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1023), 10)
        self.assertEqual(Total_Hamming_Distance(1024), 16)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            Total_Hamming_Distance('1024')
        with self.assertRaises(TypeError):
            Total_Hamming_Distance(None)
        with self.assertRaises(TypeError):
            Total_Hamming_Distance([])
