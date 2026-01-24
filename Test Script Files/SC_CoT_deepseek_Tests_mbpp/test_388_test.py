import unittest

from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(highest_Power_of_2(10), 8)
        self.assertEqual(highest_Power_of_2(32), 32)
        self.assertEqual(highest_Power_of_2(64), 64)

    def test_edge_cases(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_corner_cases(self):
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(7), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2('a')
        with self.assertRaises(ValueError):
            highest_Power_of_2(-1)
