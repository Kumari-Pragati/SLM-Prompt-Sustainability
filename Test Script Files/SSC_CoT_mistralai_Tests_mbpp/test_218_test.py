import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(min_Operations(10, 20), 9)
        self.assertEqual(min_Operations(20, 10), 9)
        self.assertEqual(min_Operations(5, 15), 13)
        self.assertEqual(min_Operations(15, 5), 13)

    def test_edge_cases(self):
        self.assertEqual(min_Operations(1, 1), 0)
        self.assertEqual(min_Operations(0, 1), 0)
        self.assertEqual(min_Operations(1, 0), math.inf)

    def test_boundary_cases(self):
        self.assertEqual(min_Operations(2**31 - 1, 2**31 - 1), 2**31 - 2)
        self.assertEqual(min_Operations(2**31 - 1, 2**31), 2**31 - 1)
        self.assertEqual(min_Operations(2**31, 2**31 - 1), 2**31 - 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Operations('a', 'b')
        with self.assertRaises(TypeError):
            min_Operations([1, 2, 3], [4, 5, 6])
        with self.assertRaises(ValueError):
            min_Operations(0, 0)
