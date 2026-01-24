import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(insert_element([], 1), [1])

    def test_single_element_list(self):
        self.assertEqual(insert_element([2], 1), [1, 2])

    def test_multiple_elements_list(self):
        self.assertEqual(insert_element([2, 3, 4], 1), [1, 2, 3, 4])

    def test_duplicate_element(self):
        self.assertEqual(insert_element([2, 2, 3, 4], 1), [1, 2, 2, 3, 4])

    def test_negative_element(self):
        self.assertEqual(insert_element([2, 3, 4], -1), [-1, 2, 3, 4])

    def test_list_with_none(self):
        self.assertEqual(insert_element([None, 2, 3, 4], 1), [1, None, 2, 3, 4])

    def test_list_with_float(self):
        self.assertEqual(insert_element([2.0, 3.0, 4.0], 1.0), [1.0, 2.0, 3.0, 4.0])

    def test_list_with_string(self):
        self.assertEqual(insert_element(['a', 'b', 'c'], 'd'), ['d', 'a', 'b', 'c'])

    def test_list_with_mixed_types(self):
        self.assertEqual(insert_element([1, 'a', 2.0, None, 3], 'b'), ['b', 1, 'a', 2.0, None, 3])

    def test_large_list(self):
        large_list = [i for i in range(1000)]
        self.assertEqual(insert_element(large_list, 1), [1] + large_list)
