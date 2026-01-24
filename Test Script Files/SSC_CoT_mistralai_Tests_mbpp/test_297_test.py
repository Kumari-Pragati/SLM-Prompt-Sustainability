import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(flatten_list([]), [])

    def test_single_element_list(self):
        self.assertListEqual(flatten_list([1]), [1])

    def test_list_with_single_nested_list(self):
        self.assertListEqual(flatten_list([1, [2]]), [1, 2])

    def test_list_with_multiple_nested_lists(self):
        self.assertListEqual(flatten_list([1, [2, [3]], 4]), [1, 2, 3, 4])

    def test_list_with_only_nested_lists(self):
        self.assertListEqual(flatten_list([[1], [2], [3]]), [1, 2, 3])

    def test_list_with_mixed_types(self):
        self.assertListEqual(flatten_list([1, [2, 3], 'a', [4, 5, 'b']]), [1, 2, 3, 'a', 4, 5, 'b'])

    def test_list_with_nested_tuples(self):
        self.assertListEqual(flatten_list([(1, 2), [(3, 4), (5, 6)]]), [1, 2, 3, 4, 5, 6])

    def test_list_with_nested_sets(self):
        self.assertListEqual(flatten_list([{1, 2}, [{'a', 'b'}, {3, 4}]]), [1, 2, 'a', 'b', 3, 4])

    def test_list_with_nested_dictionaries(self):
        self.assertListEqual(flatten_list([{'a': 1}, [{'b': 2}, {'c': 3}]]), ['a', 1, 'b', 2, 'c', 3])

    def test_list_with_empty_nested_list(self):
        self.assertListEqual(flatten_list([1, [], 3]), [1, 3])

    def test_list_with_empty_nested_tuple(self):
        self.assertListEqual(flatten_list([(1,), (), (3,)]), [1, 3])
