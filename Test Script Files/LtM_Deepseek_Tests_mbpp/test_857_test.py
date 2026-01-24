import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(listify_list([1, 2, 3]), [[1], [2], [3]])

    def test_empty_list(self):
        self.assertEqual(listify_list([]), [])

    def test_nested_list(self):
        self.assertEqual(listify_list([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_single_element_list(self):
        self.assertEqual(listify_list([5]), [[5]])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            listify_list([1, '2', 3])
