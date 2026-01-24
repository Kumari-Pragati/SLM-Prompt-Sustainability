import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(raw_heap([5, 2, 8, 12, 3]), [2, 3, 5, 8, 12])

    def test_edge(self):
        self.assertEqual(raw_heap([5]), [5])
        self.assertEqual(raw_heap([5, 5]), [5, 5])
        self.assertEqual(raw_heap([5, 5, 5]), [5, 5, 5])

    def test_empty(self):
        self.assertEqual(raw_heap([]), [])

    def test_single(self):
        self.assertEqual(raw_heap([5]), [5])

    def test_negative(self):
        self.assertEqual(raw_heap([-5, 2, 8, 12, 3]), [-12, -5, 2, 3, 8])

    def test_duplicates(self):
        self.assertEqual(raw_heap([5, 5, 5, 5]), [5, 5, 5, 5])
