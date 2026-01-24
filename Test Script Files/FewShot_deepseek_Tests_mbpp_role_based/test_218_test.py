import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Operations(10, 20), 1)

    def test_boundary_conditions(self):
        self.assertEqual(min_Operations(0, 1), 0)
        self.assertEqual(min_Operations(1, 0), 0)
        self.assertEqual(min_Operations(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(min_Operations(1, 1), 0)
        self.assertEqual(min_Operations(2, 4), 1)
        self.assertEqual(min_Operations(100, 200), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Operations("10", 20)
        with self.assertRaises(TypeError):
            min_Operations(10, "20")
        with self.assertRaises(TypeError):
            min_Operations("10", "20")
