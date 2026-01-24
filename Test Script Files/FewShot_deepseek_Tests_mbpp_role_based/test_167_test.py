import unittest
from mbpp_167_code import next_Power_Of_2

class TestNextPowerOf2(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertEqual(next_Power_Of_2(10), 16)
        self.assertEqual(next_Power_Of_2(17), 32)
        self.assertEqual(next_Power_Of_2(32), 32)

    def test_edge_conditions(self):
        self.assertEqual(next_Power_Of_2(0), 1)
        self.assertEqual(next_Power_Of_2(1), 1)
        self.assertEqual(next_Power_Of_2(2), 2)

    def test_boundary_conditions(self):
        self.assertEqual(next_Power_Of_2(2**31 - 1), 2**31)
        self.assertEqual(next_Power_Of_2(2**31), 2**32)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            next_Power_Of_2("10")
        with self.assertRaises(TypeError):
            next_Power_Of_2(None)
        with self.assertRaises(TypeError):
            next_Power_Of_2([10])
