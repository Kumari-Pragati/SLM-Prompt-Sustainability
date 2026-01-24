import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Jumps(1, 2, 3), 2)

    def test_edge_cases(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(1, 2, 0), 1)
        self.assertEqual(min_Jumps(1, 2, 1), 1)
        self.assertEqual(min_Jumps(1, 2, 2), 1)
        self.assertEqual(min_Jumps(1, 2, 3), 2)
        self.assertEqual(min_Jumps(1, 2, 4), 2)
        self.assertEqual(min_Jumps(1, 2, 5), 2)

    def test_corner_cases(self):
        self.assertEqual(min_Jumps(1, 2, 10), 2)
        self.assertEqual(min_Jumps(1, 2, 11), 2)
        self.assertEqual(min_Jumps(1, 2, 12), 2)
        self.assertEqual(min_Jumps(1, 2, 13), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Jumps("a", 2, 3)
        with self.assertRaises(TypeError):
            min_Jumps(1, "b", 3)
        with self.assertRaises(TypeError):
            min_Jumps(1, 2, "c")
