import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(increment_numerics([1, 2, 3], 1), ['2', '3', '4'])
        self.assertEqual(increment_numerics(['a', 'b', 'c'], 1), ['a', 'b', 'c'])
        self.assertEqual(increment_numerics([1, 'a', 3], 1), ['2', 'a', '4'])

    def test_edge_and_boundary_cases(self):
        self.assertEqual(increment_numerics([0, 9, 'a'], 1), ['1', '10', 'a'])
        self.assertEqual(increment_numerics([-1, 0, 1], 1), ['0', '1', '2'])
        self.assertEqual(increment_numerics([1, 2, 3], 0), ['1', '2', '3'])

    def test_special_and_corner_cases(self):
        self.assertEqual(increment_numerics(['-1', '0', '1'], 1), ['-1', '0', '2'])
        self.assertEqual(increment_numerics(['a', 'b', 'c'], -1), ['a', 'b', 'c'])
        self.assertEqual(increment_numerics([1, 2, 3], -1), ['2', '3', '4'])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            increment_numerics('a', 1)
        with self.assertRaises(TypeError):
            increment_numerics([1, 2, 3], 'a')
