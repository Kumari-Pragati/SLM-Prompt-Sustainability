import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5), 5.5)
        self.assertEqual(get_median([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 5), 3)
        self.assertEqual(get_median([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 3)

    def test_edge_cases(self):
        self.assertEqual(get_median([1, 2, 3, 4, 5], [], 5), 3)
        self.assertEqual(get_median([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 0), 3)
        self.assertEqual(get_median([], [1, 2, 3, 4, 5], 5), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_median('a', [1, 2, 3, 4, 5], 5)
        with self.assertRaises(TypeError):
            get_median([1, 2, 3, 4, 5], 'a', 5)
        with self.assertRaises(TypeError):
            get_median([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'a')
