import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 2, 2, 4, 2]), 2)

    def test_edge_cases(self):
        self.assertEqual(max_occurrences([1]), 1)
        self.assertEqual(max_occurrences([1, 1]), 1)
        self.assertEqual(max_occurrences([1, 1, 1]), 1)
        self.assertEqual(max_occurrences([1, 1, 1, 1]), 1)
        self.assertEqual(max_occurrences([2, 2, 2, 2, 2]), 2)
        self.assertEqual(max_occurrences([2, 2, 2, 2, 2, 2]), 2)

    def test_boundary_cases(self):
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_occurrences([2, 2, 2, 2, 2, 2, 2]), 2)
        self.assertEqual(max_occurrences([2, 2, 2, 2, 2, 2, 2, 2]), 2)

    def test_special_cases(self):
        self.assertEqual(max_occurrences([1, 1, 2, 1, 1, 2, 1, 2]), 2)
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2, 2, 1]), 2)
        self.assertEqual(max_occurrences([2, 2, 2, 1, 1, 1, 2, 2]), 2)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, max_occurrences, (1, 2, 3))
        self.assertRaises(TypeError, max_occurrences, [1, "2", 3])
        self.assertRaises(TypeError, max_occurrences, [1, 2, "3"])
