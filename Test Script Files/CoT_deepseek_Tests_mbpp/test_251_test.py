import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_insert_element_typical_case(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [4, 1, 4, 2, 4, 3])

    def test_insert_element_empty_list(self):
        self.assertEqual(insert_element([], 5), [5])

    def test_insert_element_single_element(self):
        self.assertEqual(insert_element([1], 2), [2, 1, 2])

    def test_insert_element_duplicate_elements(self):
        self.assertEqual(insert_element([1, 1, 2, 2], 3), [3, 1, 3, 1, 2, 3, 2, 3])

    def test_insert_element_large_list(self):
        self.assertEqual(insert_element(list(range(1, 100)), 0), [0] + list(range(1, 100)) + [0] + list(range(1, 100)))

    def test_insert_element_invalid_input(self):
        with self.assertRaises(TypeError):
            insert_element(123, 456)
