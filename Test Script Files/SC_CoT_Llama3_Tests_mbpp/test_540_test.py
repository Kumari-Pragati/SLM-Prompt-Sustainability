import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 0)

    def test_repeated(self):
        self.assertEqual(find_Diff([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 10), 0)

    def test_max_min(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)

    def test_min_max(self):
        self.assertEqual(find_Diff([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 0)

    def test_edge(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 0)

    def test_edge2(self):
        self.assertEqual(find_Diff([1, 1, 1, 1, 1], 5), 0)

    def test_edge3(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 5, 5, 5, 5, 5], 10), 0)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            find_Diff([1, 2, 3], 'a')

    def test_invalid2(self):
        with self.assertRaises(TypeError):
            find_Diff('a', 5)

    def test_invalid3(self):
        with self.assertRaises(TypeError):
            find_Diff([1, 2, 3], 5.5)
