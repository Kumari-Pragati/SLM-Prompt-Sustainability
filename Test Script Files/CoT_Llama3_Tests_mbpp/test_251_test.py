import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):
    def test_insert_element_at_start(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [4, 1, 2, 3])

    def test_insert_element_at_end(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4])

    def test_insert_element_multiple_times(self):
        self.assertEqual(insert_element([1, 2, 3], 4, 5, 6), [1, 2, 3, 4, 5, 6])

    def test_insert_element_empty_list(self):
        self.assertEqual(insert_element([], 1), [1])

    def test_insert_element_single_element(self):
        self.assertEqual(insert_element([1], 2), [1, 2])

    def test_insert_element_no_change(self):
        self.assertEqual(insert_element([1, 2, 3], 1), [1, 2, 3])

    def test_insert_element_invalid_input(self):
        with self.assertRaises(TypeError):
            insert_element("string", 1)
