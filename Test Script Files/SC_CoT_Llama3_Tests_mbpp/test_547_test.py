import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotal_Hamming_Distance(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(Total_Hamming_Distance(15), 7)

    def test_edge_cases(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)
        self.assertEqual(Total_Hamming_Distance(1), 0)
        self.assertEqual(Total_Hamming_Distance(2), 1)

    def test_special_cases(self):
        self.assertEqual(Total_Hamming_Distance(3), 1)
        self.assertEqual(Total_Hamming_Distance(4), 2)
        self.assertEqual(Total_Hamming_Distance(5), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Total_Hamming_Distance('a')
