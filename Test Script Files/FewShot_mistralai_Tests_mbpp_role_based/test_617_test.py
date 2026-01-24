import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(min_Jumps(3, 2, 1), 2)
        self.assertEqual(min_Jumps(5, 3, 2), 3)
        self.assertEqual(min_Jumps(7, 4, 3), 4)

    def test_zero(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(0, 0, 1), 1)
        self.assertEqual(min_Jumps(0, 1, 0), 1)

    def test_negative_numbers(self):
        self.assertEqual(min_Jumps(-3, -2, 1), 2)
        self.assertEqual(min_Jumps(-5, -3, 2), 3)
        self.assertEqual(min_Jumps(-7, -4, 3), 4)

    def test_edge_cases(self):
        self.assertEqual(min_Jumps(1, 0, 1), 1)
        self.assertEqual(min_Jumps(0, 1, 0), 1)
        self.assertEqual(min_Jumps(1, 1, 0), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, min_Jumps, 'a', 'b', 'd')
        self.assertRaises(TypeError, min_Jumps, 1, 'b', 'd')
        self.assertRaises(TypeError, min_Jumps, 1, 2, 'd')
