import unittest
from547_code import Total_Hamming_Distance

class TestTotalHammingDistance(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(Total_Hamming_Distance(0), 0)

    def test_one(self):
        self.assertEqual(Total_Hamming_Distance(1), 0)

    def test_two(self):
        self.assertEqual(Total_Hamming_Distance(2), 1)

    def test_three(self):
        self.assertEqual(Total_Hamming_Distance(3), 1)

    def test_four(self):
        self.assertEqual(Total_Hamming_Distance(4), 2)

    def test_five(self):
        self.assertEqual(Total_Hamming_Distance(5), 2)

    def test_six(self):
        self.assertEqual(Total_Hamming_Distance(6), 3)

    def test_seven(self):
        self.assertEqual(Total_Hamming_Distance(7), 2)

    def test_eight(self):
        self.assertEqual(Total_Hamming_Distance(8), 3)

    def test_nine(self):
        self.assertEqual(Total_Hamming_Distance(9), 2)

    def test_ten(self):
        self.assertEqual(Total_Hamming_Distance(10), 3)

    def test_twelve(self):
        self.assertEqual(Total_Hamming_Distance(12), 4)
