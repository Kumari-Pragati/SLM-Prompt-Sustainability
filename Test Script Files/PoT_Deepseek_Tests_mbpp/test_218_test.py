import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_Operations(10, 15), 4)
        self.assertEqual(min_Operations(20, 5), 4)
        self.assertEqual(min_Operations(1, 1), 0)

    def test_edge_cases(self):
        self.assertEqual(min_Operations(0, 10), 9)
        self.assertEqual(min_Operations(10, 0), 9)
        self.assertEqual(min_Operations(0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(min_Operations(1, 1000000000), 9)
        self.assertEqual(min_Operations(1000000000, 1), 9)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Operations("10", 15)
        with self.assertRaises(TypeError):
            min_Operations(10, "15")
        with self.assertRaises(TypeError):
            min_Operations("10", "15")
