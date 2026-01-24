import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(Total_Hamming_Distance(10), 12)
        self.assertEqual(Total_Hamming_Distance(15), 17)

    def test_boundary_conditions(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1), 1)

    def test_edge_cases(self):
        self.assertEqual(Total_Hamming_Distance(2), 2)
        self.assertEqual(Total_Hamming_Distance(3), 3)
        self.assertEqual(Total_Hamming_Distance(4), 4)
        self.assertEqual(Total_Hamming_Distance(7), 6)
        self.assertEqual(Total_Hamming_Distance(8), 8)

    def test_special_cases(self):
        self.assertEqual(Total_Hamming_Distance(16), 16)
        self.assertEqual(Total_Hamming_Distance(31), 28)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Total_Hamming_Distance("10")
        with self.assertRaises(ValueError):
            Total_Hamming_Distance(-5)
