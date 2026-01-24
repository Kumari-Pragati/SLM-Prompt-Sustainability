import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(insert_element([], 1), [[1]])

    def test_single_element_list(self):
        self.assertEqual(insert_element([1], 2), [[1], 2])

    def test_multiple_elements_list(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [[1, 2, 3], 4])

    def test_edge_case_empty_element(self):
        self.assertEqual(insert_element([], []), [])

    def test_edge_case_single_element(self):
        self.assertEqual(insert_element([1], []), [[1]])

    def test_edge_case_multiple_elements(self):
        self.assertEqual(insert_element([1, 2, 3], []), [[1, 2, 3]])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            insert_element(123, 1)

    def test_invalid_input_type_element(self):
        with self.assertRaises(TypeError):
            insert_element([1, 2, 3], 'abc')
