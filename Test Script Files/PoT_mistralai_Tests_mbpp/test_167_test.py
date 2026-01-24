import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(next_Power_Of_2(1), 2)
        self.assertEqual(next_Power_Of_2(2), 4)
        self.assertEqual(next_Power_Of_2(4), 8)
        self.assertEqual(next_Power_Of_2(8), 16)
        self.assertEqual(next_Power_Of_2(16), 32)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(next_Power_Of_2(0), 1)
        self.assertEqual(next_Power_Of_2(15), 32)
        self.assertEqual(next_Power_Of_2(31), 64)
        self.assertEqual(next_Power_Of_2(32), 64)
        self.assertEqual(next_Power_Of_2(127), 128)
        self.assertEqual(next_Power_Of_2(128), 128)
        self.assertEqual(next_Power_Of_2(255), 256)
        self.assertEqual(next_Power_Of_2(256), 512)
