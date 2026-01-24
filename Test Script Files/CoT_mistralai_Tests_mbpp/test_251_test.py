import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(insert_element([], 1), [1])

    def test_single_element_list(self):
        self.assertEqual(insert_element([2], 1), [2, 1])

    def test_multiple_elements_list(self):
        self.assertEqual(insert_element([2, 3, 4], 1), [2, 3, 1, 4])

    def test_duplicate_element(self):
        self.assertEqual(insert_element([2, 2, 3, 4], 1), [2, 2, 1, 3, 4])

    def test_list_with_none(self):
        self.assertEqual(insert_element([None, 2, 3, 4], 1), [None, 2, 3, 1, 4])

    def test_list_with_string(self):
        self.assertEqual(insert_element(["a", "b", "c"], "d"), ["a", "b", "d", "c"])

    def test_list_with_mixed_types(self):
        self.assertEqual(insert_element([1, "a", 2, "b", 3], 4), [1, "a", 2, "b", 4, 3])

    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            insert_element("list", 1)

    def test_invalid_input_type_element(self):
        with self.assertRaises(TypeError):
            insert_element([1], "element")
