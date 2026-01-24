import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_heap_assending(self):
        self.assertEqual(heap_assending([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        self.assertEqual(heap_assending([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(heap_assending([1]), [1])
        self.assertEqual(heap_assending([]), [])
