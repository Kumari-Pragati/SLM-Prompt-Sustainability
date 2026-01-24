import unittest
from mbpp_199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(highest_Power_of_2(10), 8)

    def test_boundary_condition(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)

    def test_edge_condition(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(32), 32)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2('a')
        with self.assertRaises(ValueError):
            highest_Power_of_2(-1)
