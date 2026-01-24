import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(Diff([1, 2, 3], [2, 3, 4]), [1, 4])
        self.assertEqual(Diff([], []), [])
        self.assertEqual(Diff([1], []), [1])
        self.assertEqual(Diff([], [1]), [1])

    def test_edge_cases(self):
        self.assertEqual(Diff([-1000000], [1]), [-1000000])
        self.assertEqual(Diff([1], [-1000000]), [-1000000])
        self.assertEqual(Diff([1000000], [1]), [1000000])
        self.assertEqual(Diff([1], [1000000]), [1000000])

    def test_complex(self):
        self.assertEqual(Diff([1, 2, 3], [3, 2, 1]), [])
        self.assertEqual(Diff([1, 2, 3], [3, 4, 1]), [2])
        self.assertEqual(Diff([1, 2, 3], [3, 4, 5]), [1, 2])
        self.assertEqual(Diff([1, 2, 3], []), [1, 2, 3])
