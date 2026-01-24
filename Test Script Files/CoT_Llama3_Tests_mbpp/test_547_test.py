import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)
        self.assertEqual(Total_Hamming_Distance(3), 2)
        self.assertEqual(Total_Hamming_Distance(4), 2)
        self.assertEqual(Total_Hamming_Distance(5), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Total_Hamming_Distance(6), 4)
        self.assertEqual(Total_Hamming_Distance(7), 6)
        self.assertEqual(Total_Hamming_Distance(8), 6)
        self.assertEqual(Total_Hamming_Distance(9), 8)
        self.assertEqual(Total_Hamming_Distance(10), 8)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Total_Hamming_Distance('a')
        with self.assertRaises(TypeError):
            Total_Hamming_Distance(None)
        with self.assertRaises(TypeError):
            Total_Hamming_Distance(1.5)
