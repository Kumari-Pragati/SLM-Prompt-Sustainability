import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Jumps(2, 3, 1), 2)

    def test_boundary_condition(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)

    def test_edge_case(self):
        self.assertEqual(min_Jumps(1, 1, 0), 1)
        self.assertEqual(min_Jumps(1, 1, 1), 1)
        self.assertEqual(min_Jumps(1, 1, 2), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Jumps('a', 3, 1)
        with self.assertRaises(TypeError):
            min_Jumps(2, 'b', 1)
        with self.assertRaises(TypeError):
            min_Jumps(2, 3, 'c')
