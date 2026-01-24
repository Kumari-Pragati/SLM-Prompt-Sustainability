import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(flatten_list([1, [2, 3], [4, [5, 6], 7]]), [1, 2, 3, 4, 5, 6, 7])

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(flatten_list([1]), [1])

    def test_nested_single_element_list(self):
        self.assertEqual(flatten_list([[1]]), [1])

    def test_nested_with_empty_list(self):
        self.assertEqual(flatten_list([[], [1, 2]]), [1, 2])

    def test_nested_with_empty_nested_list(self):
        self.assertEqual(flatten_list([[1, []]]), [1])

    def test_nested_with_empty_nested_list_at_end(self):
        self.assertEqual(flatten_list([1, [2, [3, []]]]), [1, 2, 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            flatten_list(123)
