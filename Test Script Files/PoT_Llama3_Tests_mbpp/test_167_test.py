import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(next_Power_Of_2(0), 1)
        self.assertEqual(next_Power_Of_2(1), 1)
        self.assertEqual(next_Power_Of_2(2), 4)
        self.assertEqual(next_Power_Of_2(3), 4)
        self.assertEqual(next_Power_Of_2(4), 8)
        self.assertEqual(next_Power_Of_2(5), 8)
        self.assertEqual(next_Power_Of_2(8), 16)
        self.assertEqual(next_Power_Of_2(15), 16)
        self.assertEqual(next_Power_Of_2(16), 32)
        self.assertEqual(next_Power_Of_2(31), 32)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(next_Power_Of_2(2**31 - 1), 2**32)
        self.assertEqual(next_Power_Of_2(2**31), 2**32)
        self.assertEqual(next_Power_Of_2(2**32 - 1), 2**32)
        self.assertEqual(next_Power_Of_2(2**32), 2**33)

    def test_corner_cases(self):
        self.assertEqual(next_Power_Of_2(1), 1)
        self.assertEqual(next_Power_Of_2(2), 4)
        self.assertEqual(next_Power_Of_2(3), 4)
        self.assertEqual(next_Power_Of_2(4), 8)
        self.assertEqual(next_Power_Of_2(5), 8)
        self.assertEqual(next_Power_Of_2(6), 8)
        self.assertEqual(next_Power_Of_2(7), 8)
        self.assertEqual(next_Power_Of_2(8), 16)
        self.assertEqual(next_Power_Of_2(15), 16)
        self.assertEqual(next_Power_Of_2(16), 32)
