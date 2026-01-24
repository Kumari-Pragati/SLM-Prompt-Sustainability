import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_string([1, 2, 3], 'Hello'), ['Hello1', 'Hello2', 'Hello3'])

    def test_edge_case_empty_list(self):
        self.assertEqual(add_string([], 'Hello'), [])

    def test_edge_case_empty_string(self):
        self.assertEqual(add_string([1, 2, 3], ''), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(add_string([1], 'Hello'), ['Hello1'])

    def test_edge_case_single_element_string(self):
        self.assertEqual(add_string([1, 2, 3], 'Hello'), ['Hello1', 'Hello2', 'Hello3'])

    def test_edge_case_list_with_non_integer_elements(self):
        self.assertEqual(add_string(['a', 'b', 'c'], 'Hello'), ['Helloa', 'Hellob', 'Helloc'])

    def test_edge_case_string_with_non_string_format(self):
        with self.assertRaises(TypeError):
            add_string([1, 2, 3], object())
