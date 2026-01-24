import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case(self):
        self.assertEqual(find_peak([1, 2, 3], 3), 2)

    def test_edge_case2(self):
        self.assertEqual(find_peak([5, 4, 3, 2, 1], 5), 0)

    def test_edge_case3(self):
        self.assertEqual(find_peak([1, 2, 3, 2, 1], 5), 2)

    def test_edge_case4(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6], 6), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_peak([], 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            find_peak([1, 2, 3], 'a')
