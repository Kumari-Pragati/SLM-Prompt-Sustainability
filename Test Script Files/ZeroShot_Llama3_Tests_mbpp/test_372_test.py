import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):

    def test_heap_assending(self):
        self.assertEqual(heap_assending([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(heap_assending([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(heap_assending([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(heap_assending([9, 7, 5, 3, 1]), [1, 3, 5, 7, 9])
        self.assertEqual(heap_assending([2, 1, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
