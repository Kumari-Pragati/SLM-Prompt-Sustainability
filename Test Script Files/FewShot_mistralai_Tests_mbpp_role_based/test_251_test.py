import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(insert_element([], 1), [1])

    def test_single_element_list(self):
        self.assertEqual(insert_element([2], 1), [1, 2])

    def test_multiple_elements_list(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4])

    def test_duplicate_element(self):
        self.assertEqual(insert_element([1, 2, 2], 3), [1, 2, 2, 3])

    def test_negative_list_index(self):
        with self.assertRaises(IndexError):
            insert_element([1, 2, 3], -1)

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            insert_element('string', 1)
