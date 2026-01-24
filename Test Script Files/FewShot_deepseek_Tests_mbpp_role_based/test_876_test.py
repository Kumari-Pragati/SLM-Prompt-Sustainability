import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(lcm(10, 15), 30)

    def test_boundary_conditions(self):
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(0, 10), 0)
        self.assertEqual(lcm(10, 0), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_edge_conditions(self):
        self.assertEqual(lcm(2, 2), 2)
        self.assertEqual(lcm(3, 6), 6)
        self.assertEqual(lcm(7, 7), 7)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lcm("10", 15)
        with self.assertRaises(TypeError):
            lcm(10, "15")
        with self.assertRaises(TypeError):
            lcm("10", "15")
