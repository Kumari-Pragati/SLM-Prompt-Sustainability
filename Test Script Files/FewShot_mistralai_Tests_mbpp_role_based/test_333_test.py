import unittest
from mbpp_333_code import Sort

class TestSort(unittest.TestCase):
    def test_sort_ascending(self):
        data = [('a', 1), ('b', 2), ('c', 3)]
        expected = [('a', 1), ('b', 2), ('c', 3)]
        self.assertEqual(Sort(data), expected)

    def test_sort_descending(self):
        data = [('z', 5), ('y', 4), ('x', 3)]
        expected = [('z', 5), ('y', 4), ('x', 3)]
        self.assertEqual(Sort(data, reverse=True), expected)

    def test_empty_list(self):
        self.assertEqual(Sort([]), [])

    def test_single_item(self):
        data = [('x', 1)]
        expected = [('x', 1)]
        self.assertEqual(Sort(data), expected)

    def test_duplicate_items(self):
        data = [('x', 1), ('x', 2)]
        expected = [('x', 1), ('x', 2)]
        self.assertEqual(Sort(data), expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Sort(123)
