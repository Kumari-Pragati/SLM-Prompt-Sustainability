import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_typical_usage(self):
        heap = [3, 5, 1, 6, 2]
        expected = [3, 5, 2, 6, 1]
        self.assertListEqual(heap_replace(heap, 2), expected)

    def test_empty_heap(self):
        heap = []
        self.assertRaises(ValueError, heap_replace, heap, 2)

    def test_single_element_heap(self):
        heap = [1]
        expected = [1]
        self.assertListEqual(heap_replace(heap, 2), expected)

    def test_negative_input(self):
        heap = [3, 5, 1, 6, 2]
        self.assertRaises(ValueError, heap_replace, heap, -1)

    def test_float_input(self):
        heap = [3, 5, 1, 6, 2]
        self.assertRaises(TypeError, heap_replace, heap, 2.5)

    def test_list_input(self):
        heap = [3, 5, 1, 6, 2]
        self.assertRaises(TypeError, heap_replace, heap, [1, 2, 3])
