import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(insert_element([1, 2, 3], 0), [0, 1, 0, 2, 0, 3])

    def test_empty_list(self):
        self.assertEqual(insert_element([], 5), [5])

    def test_single_element_list(self):
        self.assertEqual(insert_element([7], 8), [8, 7, 8])

    def test_insert_at_beginning(self):
        self.assertEqual(insert_element([1, 2, 3], 0), [0, 1, 0, 2, 0, 3])

    def test_insert_at_end(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4])

    def test_insert_in_middle(self):
        self.assertEqual(insert_element([1, 3], 2), [1, 2, 3])

    def test_insert_duplicates(self):
        self.assertEqual(insert_element([1, 2, 3], 2), [2, 1, 2, 2, 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            insert_element("not a list", 5)
