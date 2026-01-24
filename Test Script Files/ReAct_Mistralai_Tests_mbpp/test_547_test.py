import unittest
from mbpp_547_code import Total_HammingDistance

class TestTotalHammingDistance(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(Total_HammingDistance(0), 0)

    def test_single_bit(self):
        self.assertEqual(Total_HammingDistance(1), 1)
        self.assertEqual(Total_HammingDistance(3), 2)

    def test_powers_of_two(self):
        for i in range(1, 16):
            self.assertEqual(Total_HammingDistance(2**i), i)

    def test_odd_numbers(self):
        for i in range(1, 16):
            self.assertEqual(Total_HammingDistance(2*i + 1), 2*i + 1)

    def test_large_numbers(self):
        self.assertEqual(Total_HammingDistance(1023), 7)
        self.assertEqual(Total_HammingDistance(1024), 1)
        self.assertEqual(Total_HammingDistance(1025), 8)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            Total_HammingDistance(-1)
