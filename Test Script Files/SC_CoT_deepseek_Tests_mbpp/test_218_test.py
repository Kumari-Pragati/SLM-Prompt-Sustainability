import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Operations(10, 15), 4)

    def test_edge_case(self):
        self.assertEqual(min_Operations(0, 10), 9)
        self.assertEqual(min_Operations(10, 0), 9)
        self.assertEqual(min_Operations(0, 0), 0)

    def test_boundary_case(self):
        self.assertEqual(min_Operations(1, 1), 0)
        self.assertEqual(min_Operations(1, 2), 1)
        self.assertEqual(min_Operations(2, 1), 1)

    def test_special_case(self):
        self.assertEqual(min_Operations(10, 10), 0)
        self.assertEqual(min_Operations(10, 20), 1)
        self.assertEqual(min_Operations(20, 10), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Operations("10", 15)
        with self.assertRaises(TypeError):
            min_Operations(10, "15")
        with self.assertRaises(TypeError):
            min_Operations("10", "15")
