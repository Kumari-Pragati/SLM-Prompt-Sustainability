import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element(self):
        self.assertEqual(raw_heap([1]), [1])

    def test_multiple_elements(self):
        self.assertEqual(raw_heap([3, 1, 5, 2, 4]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(raw_heap([-3, -1, 0, 2, -4]), [-3, -1, 0, 2, -4])

    def test_floats(self):
        self.assertEqual(raw_heap([3.14, 2.71, 1.618]), [1.618, 2.71, 3.14])

    def test_duplicates(self):
        self.assertEqual(raw_heap([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_reverse_order(self):
        self.assertEqual(raw_heap(list(reversed([1, 2, 3]))), [1, 2, 3])

    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            raw_heap(123)

    def test_invalid_input_type_tuple(self):
        with self.assertRaises(TypeError):
            raw_heap((1, 2, 3))
