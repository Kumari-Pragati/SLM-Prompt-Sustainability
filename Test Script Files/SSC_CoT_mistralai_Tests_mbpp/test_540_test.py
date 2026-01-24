import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3, 4, 4, 5], 8), 2)
        self.assertEqual(find_Diff([1, 1, 1, 2, 2, 3, 4, 4, 5], 9), 1)

    def test_edge_cases(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 2, 2, 3, 4, 4, 5], 10), 3)
        self.assertEqual(find_Diff([1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5], 11), 4)
        self.assertEqual(find_Diff([], 0), 0)
        self.assertEqual(find_Diff([1], 1), 0)
        self.assertEqual(find_Diff([1, 1], 2), 0)
        self.assertEqual(find_Diff([1, 1, 1], 3), 0)
        self.assertEqual(find_Diff([1, 1, 1, 1], 4), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Diff(1, 2)
        with self.assertRaises(TypeError):
            find_Diff('abc', 2)
        with self.assertRaises(ValueError):
            find_Diff([], -1)
        with self.assertRaises(ValueError):
            find_Diff([1], -1)
        with self.assertRaises(ValueError):
            find_Diff([1, 1], -1)
        with self.assertRaises(ValueError):
            find_Diff([1, 1, 1], -1)
