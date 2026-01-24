import unittest
from mbpp_876_code import lcm

class TestLCM(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lcm(15, 20), 60)

    def test_edge_case(self):
        self.assertEqual(lcm(1, 1), 1)

    def test_boundary_case(self):
        self.assertEqual(lcm(0, 10), 0)
        self.assertEqual(lcm(10, 0), 0)

    def test_special_case(self):
        self.assertEqual(lcm(2, 4), 4)
        self.assertEqual(lcm(7, 11), 77)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lcm("15", 20)
        with self.assertRaises(TypeError):
            lcm(15, "20")
        with self.assertRaises(TypeError):
            lcm("15", "20")
