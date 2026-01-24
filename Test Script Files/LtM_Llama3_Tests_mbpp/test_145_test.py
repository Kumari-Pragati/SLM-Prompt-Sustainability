import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(max_Abs_Diff([-1, 0, 1], 3), 1)
        self.assertEqual(max_Abs_Diff([10, 20, 30, 40, 50], 5), 40)

    def test_edge(self):
        self.assertEqual(max_Abs_Diff([], 0), 0)
        self.assertEqual(max_Abs_Diff([1], 1), 0)
        self.assertEqual(max_Abs_Diff([-1], 1), 1)

    def test_max_min(self):
        self.assertEqual(max_Abs_Diff([-10, -5, 0, 5, 10], 5), 10)
        self.assertEqual(max_Abs_Diff([-10, -5, 0, 0, 10], 5), 10)
        self.assertEqual(max_Abs_Diff([-10, -5, 0, 5, 5], 5), 5)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            max_Abs_Diff('abc', 5)
        with self.assertRaises(TypeError):
            max_Abs_Diff([1, 2, 3], 'abc')
