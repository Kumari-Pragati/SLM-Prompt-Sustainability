import unittest
from mbpp_629_code import Iterable
from 629_code import Split

class TestSplitFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(Split([1, 2, 3, 4, 5]), [2, 4])
        self.assertListEqual(Split([0, 2, 4, 6, 8]), [0, 2, 4, 6, 8])
        self.assertListEqual(Split([-1, -2, -3, -4, -5]), [-1, -3, -5])

    def test_edge_and_boundary_cases(self):
        self.assertListEqual(Split([0]), [0])
        self.assertListEqual(Split([1]), [])
        self.assertListEqual(Split([2, 2]), [2])
        self.assertListEqual(Split([-1, -1]), [-1])
        self.assertListEqual(Split([-2, -2]), [-2])

    def test_invalid_input(self):
        self.assertRaises(TypeError, Split, 123)
        self.assertRaises(TypeError, Split, {'key': 'value'})
        self.assertRaises(TypeError, Split, (1, 2, 3))
