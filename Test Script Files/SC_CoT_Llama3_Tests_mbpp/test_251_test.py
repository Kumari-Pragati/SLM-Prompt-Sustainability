import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):
    def test_insert_element_typical(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4])

    def test_insert_element_edge(self):
        self.assertEqual(insert_element([1], 2), [1, 2])
        self.assertEqual(insert_element([1, 2], 3), [1, 2, 3])
        self.assertEqual(insert_element([], 1), [1])

    def test_insert_element_multiple_elements(self):
        self.assertEqual(insert_element([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_insert_element_single_element(self):
        self.assertEqual(insert_element([1], 2), [1, 2])

    def test_insert_element_empty_list(self):
        self.assertEqual(insert_element([], 1), [1])

    def test_insert_element_single_element_empty_list(self):
        self.assertEqual(insert_element([], 1), [1])

    def test_insert_element_invalid_input_type(self):
        with self.assertRaises(TypeError):
            insert_element('abc', 123)
