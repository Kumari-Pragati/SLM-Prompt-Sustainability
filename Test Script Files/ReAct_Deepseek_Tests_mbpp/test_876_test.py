import unittest
from mbpp_876_code import lcm

class TestLCM(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lcm(10, 15), 30)
        self.assertEqual(lcm(2, 7), 14)
        self.assertEqual(lcm(1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(lcm(0, 10), 10)
        self.assertEqual(lcm(10, 0), 10)
        self.assertEqual(lcm(0, 0), 0)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            lcm("10", 15)
        with self.assertRaises(TypeError):
            lcm(10, "15")
        with self.assertRaises(TypeError):
            lcm("10", "15")
