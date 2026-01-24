import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'orange', 'banana']), [('apple', 2), ('banana', 2), ('orange', 1)])

    def test_edge_case_empty_list(self):
        self.assertEqual(count_common([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_common(['apple']), [('apple', 1)])

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(count_common(['apple', 'apple', 'apple']), [('apple', 3)])

    def test_edge_case_four_or_more_elements(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'orange', 'banana', 'grape']), [('apple', 2), ('banana', 2), ('orange', 1), ('grape', 1)])

    def test_edge_case_four_or_more_elements_with_duplicates(self):
        self.assertEqual(count_common(['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'grape']), [('banana', 3), ('apple', 2), ('orange', 1), ('grape', 1)])

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            count_common(123)
