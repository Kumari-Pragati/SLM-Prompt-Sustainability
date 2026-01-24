import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Total_Hamming_Distance(10), 4)

    def test_boundary_conditions(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1), 1)
        self.assertEqual(Total_Hamming_Distance(2), 1)
        self.assertEqual(Total_Hamming_Distance(3), 2)

    def test_edge_conditions(self):
        self.assertEqual(Total_Hamming_Distance(4), 1)
        self.assertEqual(Total_Hamming_Distance(7), 4)
        self.assertEqual(Total_Hamming_Distance(8), 1)
        self.assertEqual(Total_Hamming_Distance(15), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Total_Hamming_Distance('10')
        with self.assertRaises(ValueError):
            Total_Hamming_Distance(-10)
