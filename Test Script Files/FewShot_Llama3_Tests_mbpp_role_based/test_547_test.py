import unittest
from mbpp_547_code import Total_Hamming_Distance

class TestTotal_Hamming_Distance(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(Total_Hamming_Distance(10), 9)

    def test_zero(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            Total_Hamming_Distance(-10)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            Total_Hamming_Distance('a')
