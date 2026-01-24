import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(8), 8)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(1024), 1024)
        self.assertEqual(highest_Power_of_2(1025), 1024)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(highest_Power_of_2(10), 8)
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(32), 32)
        self.assertEqual(highest_Power_of_2(64), 64)
        self.assertEqual(highest_Power_of_2(128), 128)
        self.assertEqual(highest_Power_of_2(256), 256)
        self.assertEqual(highest_Power_of_2(512), 512)
        self.assertEqual(highest_Power_of_2(7), 4)
        self.assertEqual(highest_Power_of_2(9), 8)
        self.assertEqual(highest_Power_of_2(15), 8)
        self.assertEqual(highest_Power_of_2(31), 16)
        self.assertEqual(highest_Power_of_2(63), 32)
        self.assertEqual(highest_Power_of_2(127), 64)
        self.assertEqual(highest_Power_of_2(255), 128)
        self.assertEqual(highest_Power_of_2(511), 256)
        self.assertEqual(highest_Power_of_2(1023), 512)
