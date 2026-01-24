import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_peak([20, 10, 50, 30, 40]), 3)
        self.assertEqual(find_peak([10, 20, 30, 40, 50]), 4)

    def test_edge_and_boundary(self):
        self.assertEqual(find_peak([1, 2, 3]), 2)
        self.assertEqual(find_peak([1, 2, 3, 4]), 3)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6]), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7]), 6)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8]), 7)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9]), 8)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 10)

        self.assertEqual(find_peak([5, 4, 3, 2, 1]), 1)
        self.assertEqual(find_peak([5, 4, 3, 2]), 3)
        self.assertEqual(find_peak([5, 4, 3]), 3)
        self.assertEqual(find_peak([5, 4]), 4)
        self.assertEqual(find_peak([5]), 5)

    def test_special_cases(self):
        self.assertEqual(find_peak([1, 1, 1]), 1)
        self.assertEqual(find_peak([1, 1, 2, 1]), 2)
        self.assertEqual(find_peak([1, 2, 1]), 2)
        self.assertEqual(find_peak([1, 2, 1, 2]), 2)
        self.assertEqual(find_peak([1, 2, 2, 1]), 2)
        self.assertEqual(find_peak([2, 1, 2]), 2)
        self.assertEqual(find_peak([2, 1, 2, 1]), 2)
        self.assertEqual(find_peak([2, 1, 2, 1, 2]), 2)
        self.assertEqual(find_peak([2, 1, 2, 1, 2, 1]), 2)
        self.assertEqual(find_peak([2, 1, 2, 1, 2, 1, 2]), 2)
        self.assertEqual(find_peak([2, 1, 2, 1, 2, 1, 2, 1]), 2)
        self.assertEqual(find_peak([2, 1, 2, 1, 2, 1, 2, 1, 2]), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            find_peak([])
        with self.assertRaises(ValueError):
            find_peak([1])
