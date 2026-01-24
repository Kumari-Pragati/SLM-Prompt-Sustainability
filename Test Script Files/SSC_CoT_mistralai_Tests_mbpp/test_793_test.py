import unittest
from mbpp_793_code import last

class TestLastFunction(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 5), 4)
        self.assertEqual(last([10, 20, 30, 40, 50], 50, 5), 4)

    def test_edge_cases(self):
        self.assertEqual(last([], 10, 0), -1)
        self.assertEqual(last([10], 10, 1), 0)
        self.assertEqual(last([10, 20, 30, 40], 41, 4), -1)
        self.assertEqual(last([10, 20, 30, 40], 10, 0), 0)
        self.assertEqual(last([10, 20, 30, 40], 10, 4), 3)

    def test_boundary_cases(self):
        self.assertEqual(last([1, 1, 2], 1, 3), 2)
        self.assertEqual(last([1, 1, 2], 2, 3), 2)
        self.assertEqual(last([1, 1, 2], 1, 2), 2)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, last, [1, 2, 3], 'x', 3)
        self.assertRaises(TypeError, last, [1, 2, 3], 1, -1)
        self.assertRaises(TypeError, last, [1, 2, 3], 1, 4.5)
