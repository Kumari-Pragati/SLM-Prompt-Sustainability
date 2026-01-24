import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_sort_list_empty(self):
        self.assertEqual(sort_list([]), '[]')

    def test_sort_list_single_element(self):
        for test_case in [(1, '[1]'), (10, '[10]'), (-1, '[-1]'), (-10, '[-10]')]:
            self.assertEqual(sort_list([test_case[0]]), test_case[1])

    def test_sort_list_two_elements(self):
        for test_case in [
            ((1, 2), '[1, 2]'),
            ((10, 2), '[10, 2]'),
            ((2, 1), '[1, 2]'),
            ((10, 20), '[10, 20]'),
            ((20, 10), '[20, 10]'),
            ((-1, -2), '[-2, -1]'),
            ((-10, -20), '[-10, -20]'),
            ((-2, -1), '[-2, -1]'),
        ]:
            self.assertEqual(sort_list(test_case[0]), test_case[1])

    def test_sort_list_multiple_elements(self):
        for test_case in [
            ((1, 2, 3), '[1, 2, 3]'),
            ((10, 2, 3), '[10, 2, 3]'),
            ((3, 2, 1), '[1, 2, 3]'),
            ((10, 20, 30), '[10, 20, 30]'),
            ((30, 20, 10), '[30, 20, 10]'),
            ((-1, -2, -3), '[-3, -2, -1]'),
            ((-10, -20, -30), '[-10, -20, -30]'),
            ((-30, -20, -10), '[-30, -20, -10]'),
            ((1, 10, 100), '[1, 10, 100]'),
            ((100, 10, 1), '[1, 10, 100]'),
            ((100, 100, 1), '[1, 10, 100]'),
        ]:
            self.assertEqual(sort_list(test_case[0]), test_case[1])

    def test_sort_list_mixed_types(self):
        for test_case in [
            ([1, 'a', 3], '[1, 3, a]'),
            (['1', 2, 3], '[1, 2, 3]'),
            ([1, '10', 3], '[1, 3, 10]'),
            ([1, 2, 'a'], '[1, 2, a]'),
            (['a', 2, 1], ['a, 1, 2]'),  # List items are not sorted as strings
            ([1, 2, '10'], '[1, 2, 10]'),  # '10' is considered larger than '2'
        ]:
            self.assertEqual(sort_list(test_case[0]), test_case[1])

    def test_sort_list_duplicates(self):
        for test_case in [
            ((1, 1), '[1, 1]'),
            ((10, 10), '[10, 10]'),
            ((-1, -1), '[-1, -1]'),
            ((1, 10), '[1, 10, 10]'),
            ((10, 1), '[1, 10, 10]'),
            ((-1, -10), '[-1, -10, -10]'),
            ((-10, -1), '[-10