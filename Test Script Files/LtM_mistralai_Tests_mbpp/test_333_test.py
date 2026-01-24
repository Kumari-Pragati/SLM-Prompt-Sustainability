import unittest
from mbpp_333_code import Sort

class TestSort(unittest.TestCase):

    def test_simple_sort(self):
        self.assertEqual(Sort([(1, 2), (3, 4), (0, 5)]), [(0, 1), (1, 2), (3, 4)])
        self.assertEqual(Sort([(5, 2), (3, 4), (0, 1)]), [(0, 1), (3, 4), (5, 2)])

    def test_edge_cases(self):
        self.assertEqual(Sort([]), [])
        self.assertEqual(Sort([(0, 0)]), [(0, 0)])
        self.assertEqual(Sort([(999999999, 999999999)]), [(999999999, 999999999)])

    def test_complex_sort(self):
        self.assertEqual(Sort([(100, 1), (50, 2), (200, 3), (150, 4), (250, 5)]), [(150, 4), (50, 2), (100, 1), (200, 3), (250, 5)])
        self.assertEqual(Sort([(1, 'a'), (3, 'b'), (0, 'z'), (2, 'y')]), [(0, 'z'), (1, 'a'), (2, 'y'), (3, 'b')])
