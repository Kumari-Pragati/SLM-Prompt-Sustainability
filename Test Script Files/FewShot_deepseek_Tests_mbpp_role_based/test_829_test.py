import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(second_frequent(['a', 'b', 'c', 'b', 'a']), 'b')

    def test_edge_case_single_element(self):
        self.assertEqual(second_frequent(['a']), None)

    def test_boundary_case_empty_list(self):
        self.assertEqual(second_frequent([]), None)

    def test_error_handling_non_list_input(self):
        with self.assertRaises(TypeError):
            second_frequent('not a list')

    def test_error_handling_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            second_frequent([1, 2, 3])
