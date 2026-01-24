import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element_list(self):
        self.assertEqual(raw_heap([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(raw_heap([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(raw_heap([-3, -2, -1, 0, 1]), [-3, -2, -1, 0, 1])

    def test_floats(self):
        self.assertAlmostEqual(raw_heap([1.5, 2.5, 3.5]), [1.5, 2.5, 3.5])

    def test_custom_comparator(self):
        def custom_comparator(a, b):
            return a % 2 < b % 2
        self.assertEqual(raw_heap([2, 1, 3, 0], custom_comparator), [0, 1, 2, 3])
