import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(raw_heap([3, 1, 2]), [1, 3, 2])

    def test_empty_input(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element_input(self):
        self.assertEqual(raw_heap([5]), [5])

    def test_duplicate_elements(self):
        self.assertEqual(raw_heap([3, 1, 2, 2]), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(raw_heap([-3, -1, -2]), [-3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(raw_heap([3, -1, 2]), [-1, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(raw_heap([100, 50, 150]), [50, 100, 150])
