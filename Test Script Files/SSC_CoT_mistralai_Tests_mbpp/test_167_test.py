import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(next_Power_Of_2(1), 1)
        self.assertEqual(next_Power_Of_2(2), 2)
        self.assertEqual(next_Power_Of_2(4), 4)
        self.assertEqual(next_Power_Of_2(8), 8)
        self.assertEqual(next_Power_Of_2(16), 16)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(next_Power_Of_2(0), 1)
        self.assertEqual(next_Power_Of_2(15), 16)
        self.assertEqual(next_Power_Of_2(31), 32)
        self.assertEqual(next_Power_Of_2(127), 128)
        self.assertEqual(next_Power_Of_2(128), 128)
        self.assertEqual(next_Power_Of_2(255), 256)
        self.assertEqual(next_Power_Of_2(256), 256)
        self.assertEqual(next_Power_Of_2(257), 256)
        self.assertEqual(next_Power_Of_2(511), 512)
        self.assertEqual(next_Power_Of_2(512), 512)
        self.assertEqual(next_Power_Of_2(513), 512)

    def test_special_cases(self):
        self.assertEqual(next_Power_Of_2(-1), 1)
        self.assertEqual(next_Power_Of_2(float('inf')), int(float('inf')))
        self.assertEqual(next_Power_Of_2(float('nan')), None)
