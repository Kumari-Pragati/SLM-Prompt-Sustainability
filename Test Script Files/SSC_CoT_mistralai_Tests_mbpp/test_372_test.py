import unittest
from mbpp_372_code import heap_assending

class TestHeapAssending(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(heap_assending([3, 5, 1, 7, 2]), [1, 2, 3, 5, 7])
        self.assertEqual(heap_assending([-3, -5, -1, -7, -2]), [-3, -5, -7, -2, -1])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(heap_assending([]), [])
        self.assertEqual(heap_assending([1]), [1])
        self.assertEqual(heap_assending([1, 1]), [1, 1])
        self.assertEqual(heap_assending([1, 1, 1]), [1, 1, 1])
        self.assertEqual(heap_assending([float('inf'), 1, -float('inf')]), [-float('inf'), 1, float('inf')])

    def test_duplicates(self):
        self.assertEqual(heap_assending([1, 1, 2, 2, 3]), [1, 1, 2, 2, 3])
        self.assertEqual(heap_assending([-1, -1, -2, -2, -3]), [-3, -2, -2, -1, -1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            heap_assending('not a list')
