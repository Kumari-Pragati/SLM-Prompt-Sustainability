import unittest
from mbpp_333_code import SortedList
from 333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_sort_normal(self):
        data = [('apple', 1), ('banana', 2), ('cherry', 3)]
        expected = [('apple', 1), ('banana', 2), ('cherry', 3)]
        self.assertEqual(Sort(data), expected)

    def test_sort_edge_cases(self):
        data = [('zebra', 10), ('ant', 1), ('apple', 1), ('banana', 2), ('antelope', 100)]
        expected = [('ant', 1), ('apple', 1), ('banana', 2), ('zebra', 10), ('antelope', 100)]
        self.assertEqual(Sort(data), expected)

    def test_sort_key_error(self):
        data = [('a', 1), ('b', 2), ('z', 0)]
        with self.assertRaises(TypeError):
            Sort(data)

    def test_sort_empty_list(self):
        data = []
        expected = []
        self.assertEqual(Sort(data), expected)

    def test_sort_single_item(self):
        data = [('a', 1)]
        expected = [('a', 1)]
        self.assertEqual(Sort(data), expected)

    def test_sort_list_of_tuples_with_same_second_value(self):
        data = [('apple', 1), ('banana', 1), ('cherry', 1)]
        expected = [('apple', 1), ('banana', 1), ('cherry', 1)]
        self.assertEqual(Sort(data), expected)

    def test_sort_list_of_tuples_with_same_first_value(self):
        data = [('apple', 1), ('apple', 2), ('apple', 3)]
        expected = [('apple', 1), ('apple', 2), ('apple', 3)]
        self.assertEqual(Sort(data), expected)
