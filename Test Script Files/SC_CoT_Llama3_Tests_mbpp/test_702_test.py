import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 3), 3)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 4), 4)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 5), 4)

    def test_edge_cases(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 0), 4)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 6), 1)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 5), 4)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, -1), 4)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 7), 1)

    def test_special_cases(self):
        self.assertEqual(removals([1, 1, 1, 1, 1], 5, 0), 4)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 0), 4)
        self.assertEqual(removals([1, 1, 1, 1, 1], 5, 1), 4)
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            removals(None, 5, 1)
        with self.assertRaises(TypeError):
            removals([1, 2, 3, 4, 5], None, 1)
        with self.assertRaises(TypeError):
            removals([1, 2, 3, 4, 5], 5, None)
