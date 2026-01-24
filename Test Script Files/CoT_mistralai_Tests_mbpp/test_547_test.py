import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)
        self.assertEqual(Total_Hamming_Distance(3), 1)
        self.assertEqual(Total_Hamming_Distance(4), 2)
        self.assertEqual(Total_Hamming_Distance(5), 2)
        self.assertEqual(Total_Hamming_Distance(6), 3)
        self.assertEqual(Total_Hamming_Distance(7), 2)
        self.assertEqual(Total_Hamming_Distance(8), 3)
        self.assertEqual(Total_Hamming_Distance(9), 3)
        self.assertEqual(Total_Hamming_Distance(10), 4)
        self.assertEqual(Total_Hamming_Distance(11), 4)
        self.assertEqual(Total_Hamming_Distance(12), 5)
        self.assertEqual(Total_Hamming_Distance(13), 4)
        self.assertEqual(Total_Hamming_Distance(14), 5)
        self.assertEqual(Total_Hamming_Distance(15), 5)
        self.assertEqual(Total_Hamming_Distance(16), 6)
        self.assertEqual(Total_Hamming_Distance(17), 6)
        self.assertEqual(Total_Hamming_Distance(18), 7)
        self.assertEqual(Total_Hamming_Distance(19), 7)
        self.assertEqual(Total_Hamming_Distance(20), 8)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1 << 31), 31)
        self.assertEqual(Total_Hamming_Distance(1 << 63), 63)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Total_Hamming_Distance, "not_a_number")
        self.assertRaises(TypeError, Total_Hamming_Distance, [-1])
        self.assertRaises(TypeError, Total_Hamming_Distance, [])
