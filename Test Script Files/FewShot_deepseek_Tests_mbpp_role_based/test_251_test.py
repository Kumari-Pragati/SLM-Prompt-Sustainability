import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [4, 1, 4, 2, 4, 3])

    def test_empty_list(self):
        self.assertEqual(insert_element([], 5), [5])

    def test_single_element_list(self):
        self.assertEqual(insert_element([6], 7), [7, 6, 7])

    def test_duplicate_elements(self):
        self.assertEqual(insert_element([8, 8], 9), [9, 8, 9, 8])

    def test_negative_numbers(self):
        self.assertEqual(insert_element([-1, -2], -3), [-3, -1, -3, -2])

    def test_zero(self):
        self.assertEqual(insert_element([0], 0), [0, 0])

    def test_large_numbers(self):
        self.assertEqual(insert_element([1000000, 2000000], 3000000), [3000000, 1000000, 3000000, 2000000])
