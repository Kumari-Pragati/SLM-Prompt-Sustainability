import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 2, 3, 1]), 2)
        self.assertEqual(max_occurrences([4, 4, 4, 4, 4, 4, 4]), 4)
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2, 3]), 2)

    def test_edge_cases(self):
        self.assertEqual(max_occurrences([1]), 1)
        self.assertEqual(max_occurrences([1, 1, 1]), 1)
        self.assertEqual(max_occurrences([1, 1, 1, 2]), 1)
        self.assertEqual(max_occurrences([2, 2, 2, 3]), 2)
        self.assertEqual(max_occurrences([3, 3, 3, 3, 4]), 3)

    def test_boundary_cases(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 2]), 1)
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1, 2]), 1)
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1, 1, 2]), 1)
        self.assertEqual(max_occurrences([2, 2, 2, 2, 2, 2, 3]), 2)
        self.assertEqual(max_occurrences([3, 3, 3, 3, 3, 3, 3, 4]), 3)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, max_occurrences, [1, 2, "a"])
        self.assertRaises(TypeError, max_occurrences, [1, 2, [3]])
        self.assertRaises(TypeError, max_occurrences, [1, 2, (3, 4)])
        self.assertRaises(TypeError, max_occurrences, [1, 2, None])
        self.assertRaises(TypeError, max_occurrences, [1, 2, True])
