import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(next_Power_Of_2(1), 1)
        self.assertEqual(next_Power_Of_2(2), 2)
        self.assertEqual(next_Power_Of_2(4), 4)
        self.assertEqual(next_Power_Of_2(8), 8)
        self.assertEqual(next_Power_Of_2(16), 16)
        self.assertEqual(next_Power_Of_2(32), 32)

    def test_zero(self):
        self.assertEqual(next_Power_Of_2(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(next_Power_Of_2(-1), 1)
        self.assertEqual(next_Power_Of_2(-2), 1)
        self.assertEqual(next_Power_Of_2(-4), 4)
        self.assertEqual(next_Power_Of_2(-8), 8)
        self.assertEqual(next_Power_Of_2(-16), 16)
        self.assertEqual(next_Power_Of_2(-32), 32)

    def test_edge_cases(self):
        self.assertEqual(next_Power_Of_2(127), 128)
        self.assertEqual(next_Power_Of_2(128), 128)
        self.assertEqual(next_Power_Of_2(129), 256)
        self.assertEqual(next_Power_Of_2(255), 256)
        self.assertEqual(next_Power_Of_2(256), 256)
        self.assertEqual(next_Power_Of_2(257), 512)

    def test_non_powers_of_two(self):
        self.assertEqual(next_Power_Of_2(3), 4)
        self.assertEqual(next_Power_Of_2(5), 8)
        self.assertEqual(next_Power_Of_2(7), 8)
        self.assertEqual(next_Power_Of_2(9), 16)
        self.assertEqual(next_Power_Of_2(11), 16)
        self.assertEqual(next_Power_Of_2(13), 16)
