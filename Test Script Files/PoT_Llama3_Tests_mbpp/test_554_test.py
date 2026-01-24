import unittest
from mbpp_554_code import Split

class TestSplit(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge(self):
        self.assertEqual(Split([2, 4, 6, 8, 10]), [])

    def test_edge2(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])

    def test_empty(self):
        self.assertEqual(Split([]), [])

    def test_single(self):
        self.assertEqual(Split([5]), [])

    def test_single2(self):
        self.assertEqual(Split([2]), [])

    def test_multiple(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), [1, 3, 5, 7, 9, 11])
