import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(Diff([1, 2, 3], [2, 3, 4]), [[1], [4]])
        self.assertEqual(Diff(['a', 'b', 'c'], ['b', 'c', 'd']), [['a'], ['d']])

    def test_edge_conditions(self):
        self.assertEqual(Diff([], []), [])
        self.assertEqual(Diff([1], []), [[1]])
        self.assertEqual(Diff([], [1]), [])

    def test_boundary_conditions(self):
        self.assertEqual(Diff([1], [1]), [])
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_complex_cases(self):
        self.assertEqual(Diff([1, 2, 3, 4], [3, 4, 5, 6]), [[1, 2], [5, 6]])
        self.assertEqual(Diff(['a', 'b', 'c', 'd'], ['b', 'c', 'd', 'e']), [['a'], ['e']])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Diff(123, [1, 2, 3])
        with self.assertRaises(TypeError):
            Diff([1, 2, 3], 'abc')
