import unittest
from mbpp_854_code import raw_heap

class TestRawHeap(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(raw_heap([]), [])

    def test_single_element_list(self):
        self.assertEqual(raw_heap([5]), [5])

    def test_multiple_elements_list(self):
        self.assertEqual(raw_heap([5, 3, 8, 2, 4]), [2, 3, 4, 5, 8])

    def test_negative_numbers(self):
        self.assertEqual(raw_heap([-5, -3, -8, -2, -4]), [-8, -5, -4, -3, -2])

    def test_duplicates(self):
        self.assertEqual(raw_heap([5, 5, 3, 8, 2, 4]), [2, 3, 4, 5, 5, 8])

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            raw_heap([5, 3, 'a', 2, 4])
