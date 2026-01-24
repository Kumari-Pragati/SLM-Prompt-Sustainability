import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_max_Abs_Diff(self):
        self.assertEqual(max_Abs_Diff([10, 20, 30, 40, 50], 5), 40)
        self.assertEqual(max_Abs_Diff([-10, -20, -30, -40, -50], 5), 40)
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5], 5), 4)
        self.assertEqual(max_Abs_Diff([1, 1, 1, 1, 1], 5), 0)
        self.assertEqual(max_Abs_Diff([-1, -1, -1, -1, -1], 5), 0)
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5, -6], 6), 5)
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5, 6, 7], 7), 6)
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5, -6, -7], 7), 6)

    def test_max_Abs_Diff_edge_cases(self):
        self.assertEqual(max_Abs_Diff([1], 1), 0)
        self.assertEqual(max_Abs_Diff([-1], 1), 0)
        self.assertEqual(max_Abs_Diff([1, 1], 2), 0)
        self.assertEqual(max_Abs_Diff([-1, -1], 2), 0)

    def test_max_Abs_Diff_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_Abs_Diff("test", 5)
        with self.assertRaises(TypeError):
            max_Abs_Diff([1, 2, 3], "test")
        with self.assertRaises(TypeError):
            max_Abs_Diff([1, 2, 3], 0)
