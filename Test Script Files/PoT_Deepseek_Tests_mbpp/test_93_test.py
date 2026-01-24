import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)

    def test_edge_cases(self):
        self.assertEqual(power(1, 1000), 1)
        self.assertEqual(power(-1, 1000), 1)
        self.assertEqual(power(-1, 1001), -1)

    def test_boundary_cases(self):
        self.assertEqual(power(2, 31), 2147483648)
        self.assertEqual(power(-2, 31), -2147483648)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            power("a", 2)
        with self.assertRaises(TypeError):
            power(2, "b")
