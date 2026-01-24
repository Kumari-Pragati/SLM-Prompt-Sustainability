import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(listify_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(listify_list([1]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(listify_list([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_nested_list(self):
        self.assertEqual(listify_list([[1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            listify_list("hello")

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            listify_list(123)
