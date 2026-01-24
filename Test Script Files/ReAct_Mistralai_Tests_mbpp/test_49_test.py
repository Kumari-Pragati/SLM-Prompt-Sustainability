import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            specified_element([], 0)

    def test_single_element_list(self):
        self.assertEqual(specified_element([(1, 2)], 0), [1])
        self.assertEqual(specified_element([(1, 2)], 1), [2])

    def test_multiple_elements_list(self):
        self.assertEqual(specified_element([(1, 2), (3, 4)], 0), [1, 3])
        self.assertEqual(specified_element([(1, 2), (3, 4)], 1), [2, 4])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            specified_element([(1, 2)], -1)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            specified_element([(1, 2)], len([(1, 2)]) + 1)

    def test_list_with_non_tuple_elements(self):
        with self.assertRaises(TypeError):
            specified_element([1, 2], 0)
