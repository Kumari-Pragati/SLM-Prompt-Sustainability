import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 3, 2]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 4]), 0)

    def test_edge_cases(self):
        self.assertEqual(overlapping([], []), 0)
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([], [1]), 0)
        self.assertEqual(overlapping([1], [1]), 1)

    def test_empty_lists(self):
        self.assertEqual(overlapping([], []), 0)
        self.assertEqual(overlapping([], [1]), 0)
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([1], [1]), 1)

    def test_single_element_lists(self):
        self.assertEqual(overlapping([1], [1]), 1)
        self.assertEqual(overlapping([1], [2]), 0)
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([], [1]), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            overlapping(None, [1])
        with self.assertRaises(TypeError):
            overlapping([1], None)
        with self.assertRaises(TypeError):
            overlapping(None, None)
