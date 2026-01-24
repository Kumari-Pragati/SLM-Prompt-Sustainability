import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(heap_assending([1, 2, 3]), [1, 2, 3])
        self.assertListEqual(heap_assending([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_edge_cases(self):
        self.assertListEqual(heap_assending([]), [])
        self.assertListEqual(heap_assending([1000000000]), [1000000000])
        self.assertListEqual(heap_assending([-1000000000]), [-1000000000])

    def test_complex(self):
        self.assertListEqual(heap_assending([1, -1, 0, 2, -2]), [-1, 0, 1, 2, -2])
        self.assertListEqual(heap_assending([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
