import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(min_Jumps(5, 3, 10), 1.0)
        self.assertEqual(min_Jumps(10, 5, 10), 2.0)
        self.assertEqual(min_Jumps(5, 10, 10), 1.0)

    def test_edge_cases(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(1, 1, 1), 1)
        self.assertEqual(min_Jumps(5, 3, 0), 0)

    def test_special_cases(self):
        self.assertEqual(min_Jumps(5, 3, 5), 1)
        self.assertEqual(min_Jumps(10, 5, 10), 2)
        self.assertEqual(min_Jumps(5, 10, 10), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Jumps('a', 'b', 'd')
        with self.assertRaises(TypeError):
            min_Jumps(5, 'b', 'd')
        with self.assertRaises(TypeError):
            min_Jumps(5, 3, 'd')
