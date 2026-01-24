import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11), 3)

    def test_edge_case(self):
        self.assertEqual(min_jumps([0, 0, 0, 0, 0], 5), 5)

    def test_boundary_case(self):
        self.assertEqual(min_jumps([], 0), float('inf'))
        self.assertEqual(min_jumps([1], 1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_jumps("not a list", 1)
        with self.assertRaises(TypeError):
            min_jumps([1, 2, 3], "not an integer")
