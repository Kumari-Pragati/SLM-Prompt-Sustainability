import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case_empty_list(self):
        self.assertIsNone(second_frequent([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(second_frequent([1]), None)

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(second_frequent([1, 1, 1]), 1)

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 4, 4, 4]), 4)

    def test_edge_case_multiple_elements_list_with_duplicates(self):
        self.assertEqual(second_frequent([1, 1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            second_frequent("hello")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            second_frequent(123)
