import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_Operations(10, 15), 4)
        self.assertEqual(min_Operations(5, 10), 3)

    def test_boundary_conditions(self):
        self.assertEqual(min_Operations(0, 10), 9)
        self.assertEqual(min_Operations(10, 0), 9)
        self.assertEqual(min_Operations(0, 0), 0)
        self.assertEqual(min_Operations(1, 1), 0)

    def test_edge_cases(self):
        self.assertEqual(min_Operations(2, 4), 2)
        self.assertEqual(min_Operations(4, 2), 2)
        self.assertEqual(min_Operations(100, 100), 99)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Operations("10", 15)
        with self.assertRaises(TypeError):
            min_Operations(10, "15")
        with self.assertRaises(TypeError):
            min_Operations("10", "15")
