import unittest
from mbpp_251_code import deepcopy
from 251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(insert_element([], 1), [1])

    def test_single_element_list(self):
        self.assertEqual(insert_element([2], 1), [1, 2])

    def test_multiple_elements_list(self):
        self.assertEqual(insert_element([2, 3], 1), [1, 2, 3])

    def test_duplicate_element(self):
        self.assertEqual(insert_element([2, 2], 1), [1, 2, 2])

    def test_list_with_duplicate_index(self):
        self.assertEqual(insert_element([2, 2, 2], 1), [1, 2, 2, 2])

    def test_list_with_multiple_insertions(self):
        self.assertEqual(insert_element([2, 3], 1), [1, 2, 3])
        self.assertEqual(insert_element([1, 2, 3], 0), [0, 1, 2, 3])
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4])

    def test_list_with_negative_index(self):
        self.assertEqual(insert_element([2, 3], -1), [3, 2])
        self.assertEqual(insert_element([2, 3], -2), [2, 3])

    def test_list_with_out_of_range_index(self):
        self.assertEqual(insert_element([2, 3], 5), [2, 3])
        self.assertEqual(insert_element([2, 3], len([2, 3]) + 1), [2, 3])

    def test_list_with_none_type_element(self):
        self.assertEqual(insert_element([2, 3], None), [None, 2, 3])

    def test_list_with_list_type_element(self):
        self.assertEqual(insert_element([[2], 3], [1]), [[1, 2], 3])
