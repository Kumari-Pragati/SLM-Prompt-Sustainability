import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(min_Jumps(5, 3, 2), 3)
        self.assertEqual(min_Jumps(3, 5, 2), 3)
        self.assertEqual(min_Jumps(5, 3, 3), 2)
        self.assertEqual(min_Jumps(3, 5, 3), 2)

    def test_edge_cases(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(1, 0, 1), 1)
        self.assertEqual(min_Jumps(0, 1, 1), 1)
        self.assertEqual(min_Jumps(1, 1, 0), 1)
        self.assertEqual(min_Jumps(1, 1, 1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(min_Jumps(1, 2, 1), 2)
        self.assertEqual(min_Jumps(2, 1, 1), 2)
        self.assertEqual(min_Jumps(2, 2, 1), 3)
        self.assertEqual(min_Jumps(1, 2, 2), 2)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, min_Jumps, 'a', 'b', 'd')
        self.assertRaises(TypeError, min_Jumps, 1.5, 'b', 'd')
        self.assertRaises(TypeError, min_Jumps, a, b, 0)
