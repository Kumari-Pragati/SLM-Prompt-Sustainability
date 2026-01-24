import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(0.5, 2), 0.25)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(1, 0), 1)
        self.assertEqual(power(2, -1), 2)
        self.assertEqual(power(-2, -1), -2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            power('a', 2)
        with self.assertRaises(TypeError):
            power(2, 'b')
