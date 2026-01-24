import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_Min_Diff([1, 3, 5, 7], 4), 2)
        self.assertEqual(find_Min_Diff([10, 20, 30, 40], 4), 10)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4], 4), 1)
        self.assertEqual(find_Min_Diff([5, 5, 5, 5], 4), 0)

    def test_edge(self):
        self.assertEqual(find_Min_Diff([1, 1, 1, 1], 4), 0)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4], 4), 1)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6], 6), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            find_Min_Diff([], 0)
        with self.assertRaises(TypeError):
            find_Min_Diff([1, 2, 3], 'a')
        with self.assertRaises(TypeError):
            find_Min_Diff([1, 2, 3], -1)
