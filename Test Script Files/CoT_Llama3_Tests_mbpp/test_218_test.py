import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(min_Operations(2, 4), 1)
        self.assertEqual(min_Operations(3, 6), 1)
        self.assertEqual(min_Operations(4, 8), 1)

    def test_edge_cases(self):
        self.assertEqual(min_Operations(1, 1), 0)
        self.assertEqual(min_Operations(2, 2), 1)
        self.assertEqual(min_Operations(3, 3), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Operations('a', 4)
        with self.assertRaises(TypeError):
            min_Operations(2, 'b')

    def test_boundary_conditions(self):
        self.assertEqual(min_Operations(0, 0), 0)
        self.assertEqual(min_Operations(0, 1), 0)
        self.assertEqual(min_Operations(1, 0), 0)
