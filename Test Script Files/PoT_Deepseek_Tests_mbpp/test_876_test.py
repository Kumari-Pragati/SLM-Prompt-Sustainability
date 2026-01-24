import unittest
from mbpp_876_code import lcm

class TestLCM(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lcm(15, 20), 60)
        self.assertEqual(lcm(7, 11), 77)
        self.assertEqual(lcm(1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(lcm(0, 10), 10)
        self.assertEqual(lcm(10, 0), 10)
        self.assertEqual(lcm(0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(lcm(2147483647, 1), 2147483647)
        self.assertEqual(lcm(1, 2147483647), 2147483647)
        self.assertEqual(lcm(2147483647, 2147483647), 2147483647)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lcm("15", 20)
        with self.assertRaises(TypeError):
            lcm(15, "20")
        with self.assertRaises(TypeError):
            lcm("15", "20")
