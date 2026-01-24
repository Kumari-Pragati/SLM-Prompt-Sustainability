import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_sort_typical_case(self):
        data = [('apple', 1), ('banana', 2), ('cherry', 3)]
        result = Sort(data)
        expected = [('apple', 1), ('banana', 2), ('cherry', 3)]
        self.assertEqual(result, expected)

    def test_sort_edge_case_empty_list(self):
        data = []
        result = Sort(data)
        self.assertEqual(result, [])

    def test_sort_edge_case_single_item(self):
        data = [('orange', 4)]
        result = Sort(data)
        expected = [('orange', 4)]
        self.assertEqual(result, expected)

    def test_sort_edge_case_duplicate_items(self):
        data = [('grape', 5), ('grape', 5), ('grape', 5)]
        result = Sort(data)
        expected = [('grape', 5), ('grape', 5), ('grape', 5)]
        self.assertEqual(result, expected)

    def test_sort_edge_case_reverse_order(self):
        data = [('zebra', 0), ('antelope', 1), ('lion', 2)]
        result = Sort(data)
        expected = [('antelope', 1), ('lion', 2), ('zebra', 0)]
        self.assertEqual(result, expected)

    def test_sort_invalid_input_not_list(self):
        with self.assertRaises(TypeError):
            Sort('not a list')

    def test_sort_invalid_input_not_tuple(self):
        with self.assertRaises(TypeError):
            Sort([1, 2, 3])
