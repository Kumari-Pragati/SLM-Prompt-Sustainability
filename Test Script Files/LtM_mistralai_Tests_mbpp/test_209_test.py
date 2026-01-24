import unittest
from mbpp_209_code import heap_replace

class TestHeapReplace(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(heap_replace([1, 2, 3], 4), [1, 2, 4])
        self.assertEqual(heap_replace([4, 3, 2, 1], 0), [0, 2, 3, 4])

    def test_edge_cases(self):
        self.assertEqual(heap_replace([], 1), [1])
        self.assertEqual(heap_replace([1], 2), [2])
        self.assertEqual(heap_replace([1, 2], float('inf')), [2, 1])
        self.assertEqual(heap_replace([float('inf')], float('-inf')), [float('-inf')])

    def test_complex(self):
        self.assertEqual(heap_replace([float('inf'), 2, 1], float('-inf')), [float('-inf'), 2, 1])
        self.assertEqual(heap_replace([-float('inf'), 2, 1], float('inf')), [float('inf'), 2, 1])
        self.assertEqual(heap_replace([-float('inf'), float('inf')], 0), [0, float('inf')])
