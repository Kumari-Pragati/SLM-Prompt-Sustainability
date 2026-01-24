import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)
        self.assertEqual(first_odd([5, 3, 2, 8, 1]), 3)
        self.assertEqual(first_odd([1, -1, 3, -5, 7]), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_odd([]), -1)
        self.assertEqual(first_odd([0]), -1)
        self.assertEqual(first_odd([2, 2, 2]), -1)
        self.assertEqual(first_odd([-2, -2, -2]), -1)
        self.assertEqual(first_odd([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(first_odd([-1, -2, -3, -4, -5]), -1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, first_odd, "string")
        self.assertRaises(TypeError, first_odd, [1.5])
