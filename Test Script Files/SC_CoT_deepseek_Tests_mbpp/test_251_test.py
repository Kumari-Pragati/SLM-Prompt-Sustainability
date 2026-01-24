import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [4, 1, 2, 3, 1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(insert_element([], 5), [5])

    def test_single_element_list(self):
        self.assertEqual(insert_element([7], 8), [8, 7, 8])

    def test_large_list(self):
        large_list = list(range(1, 1001))
        self.assertEqual(insert_element(large_list, 0), [0] + large_list + [0] + large_list)

    def test_negative_elements(self):
        self.assertEqual(insert_element([-1, -2, -3], -4), [-4, -1, -2, -3, -1, -2, -3])

    def test_zero(self):
        self.assertEqual(insert_element([0, 1, 2], 0), [0, 0, 1, 2, 0, 1, 2])

    def test_invalid_input_not_list(self):
        with self.assertRaises(TypeError):
            insert_element("not a list", 4)

    def test_invalid_input_list_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            insert_element(["a", "b", "c"], 4)
