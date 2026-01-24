import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):
    def test_overlapping_normal(self):
        self.assertEqual(overlapping([1, 2, 3], [3, 4, 5]), 1)
        self.assertEqual(overlapping([1, 1, 2], [1, 2, 3]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3, 4]), 0)

    def test_overlapping_edge_cases(self):
        self.assertEqual(overlapping([], []), 0)
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([], [1]), 0)
        self.assertEqual(overlapping([1], [1]), 1)

    def test_overlapping_boundary_cases(self):
        self.assertEqual(overlapping([0, 0, 0], [1, 1, 1]), 0)
        self.assertEqual(overlapping([1, 1, 1], [0, 0, 0]), 0)
        self.assertEqual(overlapping([1, 1, 1], [1, 0, 1]), 1)
        self.assertEqual(overlapping([1, 0, 1], [1, 1, 1]), 1)

    def test_overlapping_invalid_inputs(self):
        self.assertRaises(TypeError, overlapping, [1, 2, 3], "list2")
        self.assertRaises(TypeError, overlapping, "list1", [1, 2, 3])
