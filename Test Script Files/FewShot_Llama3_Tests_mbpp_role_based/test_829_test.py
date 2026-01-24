import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(second_frequent(['a', 'b', 'c', 'a', 'b']), 'b')

    def test_edge_case_empty_list(self):
        self.assertIsNone(second_frequent([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(second_frequent(['a']), 'a')

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(second_frequent(['a', 'a', 'a']), 'a')

    def test_edge_case_multiple_elements_with_duplicates(self):
        self.assertEqual(second_frequent(['a', 'b', 'c', 'a', 'b', 'c']), 'b')

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            second_frequent(123)
