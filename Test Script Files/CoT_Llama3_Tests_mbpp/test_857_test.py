import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):
    def test_listify_list_empty_list(self):
        self.assertEqual(listify_list([]), [])

    def test_listify_list_single_element(self):
        self.assertEqual(listify_list([1]), [[1]])

    def test_listify_list_multiple_elements(self):
        self.assertEqual(listify_list([1, 2, 3]), [[1], [2], [3]])

    def test_listify_list_nested_list(self):
        self.assertEqual(listify_list([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_listify_list_mixed_types(self):
        self.assertEqual(listify_list([1, 'a', 3.14]), [[1], ['a'], [3.14]])

    def test_listify_list_invalid_input(self):
        with self.assertRaises(TypeError):
            listify_list('not a list')
