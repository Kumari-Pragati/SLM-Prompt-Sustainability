import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Total_Hamming_Distance(10), 3)

    def test_edge_case_zero(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(Total_Hamming_Distance(1), 0)

    def test_edge_case_power_of_two(self):
        self.assertEqual(Total_Hamming_Distance(4), 1)

    def test_large_number(self):
        self.assertEqual(Total_Hamming_Distance(1000), 14)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            Total_Hamming_Distance(-1)
