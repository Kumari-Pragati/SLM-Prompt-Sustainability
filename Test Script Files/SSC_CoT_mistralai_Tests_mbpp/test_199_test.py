import unittest
from mbpp_199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(16), 16)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(15), 16)
        self.assertEqual(highest_Power_of_2(255), 256)
        self.assertEqual(highest_Power_of_2(256), 256)
        self.assertEqual(highest_Power_of_2(257), 256)
        self.assertEqual(highest_Power_of_2(2147483647), 2147483648)

    def test_special_cases(self):
        self.assertEqual(highest_Power_of_2(2147483648), 2147483648)
        self.assertEqual(highest_Power_of_2(-1), 0)
        self.assertEqual(highest_Power_of_2(-2), 0)
        self.assertEqual(highest_Power_of_2(-3), 0)
