import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(Diff([]), [])
        self.assertEqual(Diff([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(Diff([1, 2, 3], []), [1, 2, 3])

    def test_single_element_lists(self):
        self.assertEqual(Diff([1], [1]), [])
        self.assertEqual(Diff([1], [2]), [1])
        self.assertEqual(Diff([2], [1]), [2])

    def test_same_lists(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_different_lengths(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2]), [3])
        self.assertEqual(Diff([1, 2], [1, 2, 3]), [3])

    def test_containment(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2]), [3])
        self.assertEqual(Diff([1, 2], [1, 3]), [2])

    def test_edge_cases(self):
        self.assertEqual(Diff(range(10), range(20)), list(range(10, 20)))
        self.assertEqual(Diff(range(20), range(10)), list(range(20, 30)))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Diff, 1, 2.5)
        self.assertRaises(TypeError, Diff, '1', '2')
