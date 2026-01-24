import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_insert_element_simple(self):
        self.assertEqual(insert_element([1, 2, 3], 0), [0, 1, 0, 2, 0, 3])

    def test_insert_element_empty(self):
        self.assertEqual(insert_element([], 5), [5])

    def test_insert_element_single_element(self):
        self.assertEqual(insert_element([7], 8), [8, 7])

    def test_insert_element_large_numbers(self):
        self.assertEqual(insert_element([1000, 2000], 500), [500, 1000, 500, 2000])

    def test_insert_element_negative_numbers(self):
        self.assertEqual(insert_element([-1, -2], -3), [-3, -1, -3, -2])

    def test_insert_element_duplicate_elements(self):
        self.assertEqual(insert_element([1, 1, 2], 1), [1, 1, 1, 2])
