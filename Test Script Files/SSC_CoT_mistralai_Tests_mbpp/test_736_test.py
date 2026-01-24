import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(left_insertion([1, 3, 5], 2), 1)
        self.assertEqual(left_insertion([5, 3, 1], 2), 1)
        self.assertEqual(left_insertion([1, 2, 3], 1), 0)
        self.assertEqual(left_insertion([3, 2, 1], 3), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(left_insertion([], 0), 0)
        self.assertEqual(left_insertion([0], 0), 0)
        self.assertEqual(left_insertion([0], 1), 1)
        self.assertEqual(left_insertion([1], 0), 0)
        self.assertEqual(left_insertion([1], 1), 0)
        self.assertEqual(left_insertion([1, 0], 1), 0)
        self.assertEqual(left_insertion([1, 0], 2), 1)

    def test_negative_numbers(self):
        self.assertEqual(left_insertion([-1, -3, -5], -2), 0)
        self.assertEqual(left_insertion([-5, -3, -1], -2), 0)
        self.assertEqual(left_insertion([-1, -2, -3], -1), 0)
        self.assertEqual(left_insertion([-3, -2, -1], -3), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            left_insertion(1.23, 2)
        with self.assertRaises(TypeError):
            left_insertion('abc', 2)
        with self.assertRaises(TypeError):
            left_insertion([1, 2, 3], 'x')
