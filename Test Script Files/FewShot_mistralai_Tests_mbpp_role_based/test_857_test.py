import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(listify_list([]), [[]])

    def test_single_element_list(self):
        self.assertEqual(listify_list([1]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(listify_list([1, 2, 3]), [[1], [2], [3]])

    def test_list_of_lists(self):
        self.assertEqual(listify_list([[1], [2], [3]]), [[[1]], [[2]], [[3]]])

    def test_list_with_non_list_element(self):
        with self.assertRaises(TypeError):
            listify_list([1, "string"])
