import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_mixed_list([3, 'a', 1, 'b', 2]), [1, 2, 3, 'a', 'b'])

    def test_empty_list(self):
        self.assertEqual(sort_mixed_list([]), [])

    def test_list_with_same_types(self):
        self.assertEqual(sort_mixed_list(['a', 'b', 'c']), ['a', 'b', 'c'])
        self.assertEqual(sort_mixed_list([1, 2, 3]), [1, 2, 3])

    def test_list_with_one_element(self):
        self.assertEqual(sort_mixed_list([1]), [1])
        self.assertEqual(sort_mixed_list(['a']), ['a'])

    def test_list_with_mixed_types(self):
        self.assertEqual(sort_mixed_list([3, 'b', 1, 'a', 2]), [1, 2, 3, 'a', 'b'])
