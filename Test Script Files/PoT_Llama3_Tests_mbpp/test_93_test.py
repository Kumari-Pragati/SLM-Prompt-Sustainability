import unittest
from mbpp_93_code import power

class TestPower(unittest.TestCase):
    def test_power_typical(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(4, 1), 4)
        self.assertEqual(power(5, 0), 1)

    def test_power_edge(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(1, 0), 1)
        self.assertEqual(power(1, 1), 1)

    def test_power_invalid(self):
        with self.assertRaises(TypeError):
            power('a', 2)
        with self.assertRaises(TypeError):
            power(2, 'b')
