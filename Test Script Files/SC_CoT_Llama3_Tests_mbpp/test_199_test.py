import unittest
from mbpp_199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(32), 32)
        self.assertEqual(highest_Power_of_2(64), 64)

    def test_edge_cases(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_boundary_cases(self):
        self.assertEqual(highest_Power_of_2(128), 128)
        self.assertEqual(highest_Power_of_2(256), 128)

    def test_special_cases(self):
        self.assertEqual(highest_Power_of_2(15), 8)
        self.assertEqual(highest_Power_of_2(31), 16)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2('a')
        with self.assertRaises(TypeError):
            highest_Power_of_2(None)
