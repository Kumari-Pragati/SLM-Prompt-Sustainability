import unittest
from mbpp_199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(8), 8)

    def test_edge_cases(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(15), 16)
        self.assertEqual(highest_Power_of_2(255), 256)
        self.assertEqual(highest_Power_of_2(256), 256)
        self.assertEqual(highest_Power_of_2(257), 256)

    def test_complex(self):
        self.assertEqual(highest_Power_of_2(2147483647), 2147483648)
        self.assertEqual(highest_Power_of_2(2147483648), 2147483648)
        self.assertEqual(highest_Power_of_2(2147483649), 2147483648)
