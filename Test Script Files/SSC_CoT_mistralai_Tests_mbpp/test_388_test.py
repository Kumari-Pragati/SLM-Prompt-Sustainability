import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(32), 32)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(3), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(5), 4)
        self.assertEqual(highest_Power_of_2(6), 6)
        self.assertEqual(highest_Power_of_2(7), 4)
        self.assertEqual(highest_Power_of_2(255), 255)
        self.assertEqual(highest_Power_of_2(256), 256)
        self.assertEqual(highest_Power_of_2(511), 512)
        self.assertEqual(highest_Power_of_2(512), 512)
        self.assertEqual(highest_Power_of_2(1023), 1024)
        self.assertEqual(highest_Power_of_2(1024), 1024)

    def test_special_cases(self):
        self.assertEqual(highest_Power_of_2(-1), 0)
        self.assertEqual(highest_Power_of_2(-2), 0)
        self.assertEqual(highest_Power_of_2(-3), 0)
        self.assertEqual(highest_Power_of_2(-4), 0)
        self.assertEqual(highest_Power_of_2(-5), 0)
        self.assertEqual(highest_Power_of_2(-6), 0)
        self.assertEqual(highest_Power_of_2(-7), 0)
        self.assertEqual(highest_Power_of_2(-8), 0)
