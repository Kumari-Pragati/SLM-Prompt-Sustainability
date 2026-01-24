import unittest
from mbpp_199_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(highest_Power_of_2(10), 8)
        self.assertEqual(highest_Power_of_2(16), 16)
        self.assertEqual(highest_Power_of_2(32), 32)

    def test_edge_cases(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(2), 2)

    def test_boundary_conditions(self):
        self.assertEqual(highest_Power_of_2(31), 32)
        self.assertEqual(highest_Power_of_2(33), 32)
        self.assertEqual(highest_Power_of_2(63), 64)
        self.assertEqual(highest_Power_of_2(64), 64)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2('a')
        with self.assertRaises(TypeError):
            highest_Power_of_2(None)
        with self.assertRaises(TypeError):
            highest_Power_of_2([])
        with self.assertRaises(TypeError):
            highest_Power_of_2({})
