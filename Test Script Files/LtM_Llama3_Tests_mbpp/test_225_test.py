import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 1)
        self.assertEqual(find_Min([5, 4, 3, 2, 1], 0, 4), 1)
        self.assertEqual(find_Min([1, 1, 1, 1, 1], 0, 4), 1)

    def test_edge(self):
        self.assertEqual(find_Min([1], 0, 0), 1)
        self.assertEqual(find_Min([1, 2], 0, 1), 1)
        self.assertEqual(find_Min([1, 2, 3], 0, 2), 1)
        self.assertEqual(find_Min([1, 2, 3, 4], 0, 3), 1)
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 1)

    def test_edge2(self):
        self.assertEqual(find_Min([], 0, 0), None)
        self.assertEqual(find_Min([1], 0, 0), 1)
        self.assertEqual(find_Min([1, 2], 0, 1), 1)
        self.assertEqual(find_Min([1, 2, 3], 0, 2), 1)
        self.assertEqual(find_Min([1, 2, 3, 4], 0, 3), 1)
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 1)

    def test_complex(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5, 6], 0, 5), 1)
        self.assertEqual(find_Min([6, 5, 4, 3, 2, 1], 0, 5), 1)
        self.assertEqual(find_Min([1, 2, 3, 4, 5, 6, 7], 0, 6), 1)
        self.assertEqual(find_Min([7, 6, 5, 4, 3, 2, 1], 0, 6), 1)
