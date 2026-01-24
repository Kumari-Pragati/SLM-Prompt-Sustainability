import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_positive_scenarios(self):
        self.assertEqual(min_Jumps(1, 2, 1), 2)
        self.assertEqual(min_Jumps(2, 3, 2), 3)
        self.assertEqual(min_Jumps(4, 5, 3), 5)
        self.assertEqual(min_Jumps(6, 7, 4), 6)

    def test_edge_scenarios(self):
        self.assertEqual(min_Jumps(0, 1, 0), 0)
        self.assertEqual(min_Jumps(1, 0, 0), 0)
        self.assertEqual(min_Jumps(1, 1, 0), 1)
        self.assertEqual(min_Jumps(1, 1, 1), 1)
        self.assertEqual(min_Jumps(2, 2, 2), 1)

    def test_boundary_scenarios(self):
        self.assertEqual(min_Jumps(1, 2, 1), 2)
        self.assertEqual(min_Jumps(2, 1, 1), 2)
        self.assertEqual(min_Jumps(1, 1, 1), 1)
        self.assertEqual(min_Jumps(0, 1, 1), 1)
        self.assertEqual(min_Jumps(1, 0, 1), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, min_Jumps, "a", "b", "d")
        self.assertRaises(TypeError, min_Jumps, 1, "b", "d")
        self.assertRaises(TypeError, min_Jumps, 1, 2, "d")
