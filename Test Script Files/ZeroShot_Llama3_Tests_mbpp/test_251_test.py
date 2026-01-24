import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_insert_element(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4])
        self.assertEqual(insert_element([1, 2, 3], 4), [4, 1, 2, 3])
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 4, 2, 3])
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 4, 3])
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4, 4])
        self.assertEqual(insert_element([1, 2, 3], 4), [4, 1, 2, 3, 4])
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 4, 2, 3, 4])
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 4, 3, 4])
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4, 4, 4])

    def test_insert_element_empty_list(self):
        self.assertEqual(insert_element([], 4), [4])
        self.assertEqual(insert_element([], 4), [4, 4])
        self.assertEqual(insert_element([], 4), [4, 4, 4])

    def test_insert_element_single_element(self):
        self.assertEqual(insert_element([1], 4), [1, 4])
        self.assertEqual(insert_element([1], 4), [4, 1])
        self.assertEqual(insert_element([1], 4), [1, 4, 4])

    def test_insert_element_multiple_elements(self):
        self.assertEqual(insert_element([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(insert_element([1, 2, 3], [4, 5, 6]), [4, 1, 2, 3, 5, 6])
        self.assertEqual(insert_element([1, 2, 3], [4, 5, 6]), [1, 4, 2, 3, 5, 6])
        self.assertEqual(insert_element([1, 2, 3], [4, 5, 6]), [1, 2, 4, 3, 5, 6])
        self.assertEqual(insert_element([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6, 6])
