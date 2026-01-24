import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(min_Jumps(1, 2, 3), 1.0)
        self.assertEqual(min_Jumps(2, 3, 4), 1.0)
        self.assertEqual(min_Jumps(3, 4, 5), 1.0)

    def test_edge_cases(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(0, 1, 0), 0)
        self.assertEqual(min_Jumps(1, 2, 1), 1)
        self.assertEqual(min_Jumps(2, 3, 2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Jumps('a', 'b', 'd')
        with self.assertRaises(TypeError):
            min_Jumps(1, 'b', 'd')
        with self.assertRaises(TypeError):
            min_Jumps(1, 2, 'd')
