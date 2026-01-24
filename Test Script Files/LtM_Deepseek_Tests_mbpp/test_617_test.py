import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_Jumps(1, 2, 3), 2)
        self.assertEqual(min_Jumps(5, 5, 10), 1)
        self.assertEqual(min_Jumps(0, 0, 0), 0)

    def test_edge_conditions(self):
        self.assertEqual(min_Jumps(0, 10, 10), 2)
        self.assertEqual(min_Jumps(10, 0, 10), 2)
        self.assertEqual(min_Jumps(10, 10, 0), 1)
        self.assertEqual(min_Jumps(10, 10, 10), 2)

    def test_boundary_conditions(self):
        self.assertEqual(min_Jumps(0, 10, 11), 2)
        self.assertEqual(min_Jumps(10, 0, 11), 2)
        self.assertEqual(min_Jumps(10, 10, 11), 2)
        self.assertEqual(min_Jumps(0, 0, 1), 0)
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(10, 10, 10), 1)

    def test_complex_cases(self):
        self.assertEqual(min_Jumps(1, 2, 5), 2)
        self.assertEqual(min_Jumps(2, 1, 5), 2)
        self.assertEqual(min_Jumps(1, 2, 4), 2)
        self.assertEqual(min_Jumps(2, 1, 4), 2)
        self.assertEqual(min_Jumps(1, 2, 3), 2)
        self.assertEqual(min_Jumps(2, 1, 3), 2)
