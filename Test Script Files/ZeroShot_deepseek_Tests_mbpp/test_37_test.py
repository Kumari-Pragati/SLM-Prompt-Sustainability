import unittest
from mbpp_37_code import sort_mixed_list

class TestSortMixedList(unittest.TestCase):

    def test_sort_mixed_list(self):
        self.assertEqual(sort_mixed_list([3, 'a', 1, 'b', 2]), [1, 2, 3, 'a', 'b'])
        self.assertEqual(sort_mixed_list(['b', 'a', 2, 1]), [1, 2, 'a', 'b'])
        self.assertEqual(sort_mixed_list([1, 'b', 'a', 2]), [1, 2, 'a', 'b'])
        self.assertEqual(sort_mixed_list([]), [])
        self.assertEqual(sort_mixed_list([1]), [1])
        self.assertEqual(sort_mixed_list(['a']), ['a'])
        self.assertEqual(sort_mixed_list([1, 'a']), [1, 'a'])
        self.assertEqual(sort_mixed_list(['a', 1]), [1, 'a'])
