import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_replace_list(self):
        self.assertEqual(replace_list([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(replace_list(['a', 'b', 'c'], ['d', 'e', 'f']), ['a', 'b', 'c', 'd', 'e', 'f'])
        self.assertEqual(replace_list([True, False], [True, False]), [True, False, True, False])
        self.assertEqual(replace_list([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(replace_list([1, 2, 3], []), [1, 2, 3])
