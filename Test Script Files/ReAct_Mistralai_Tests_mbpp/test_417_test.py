import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(group_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(group_tuples([(1, 2)]), [(1, 2)])

    def test_multiple_tuples_same_first_element(self):
        self.assertEqual(group_tuples([(1, 2), (1, 3), (1, 4)]), [(1, [2, 3, 4])])

    def test_multiple_tuples_different_first_elements(self):
        self.assertEqual(group_tuples([(1, 2), (3, 4)]), [(1, [2]), (3, [4])])

    def test_mixed_tuples_and_lists(self):
        self.assertEqual(group_tuples([(1, 2), [3, 4], (5, 6)]), [(1, [2]), [3, 4], (5, 6)])

    def test_tuples_with_single_element(self):
        self.assertEqual(group_tuples([(1), (2)]), [(1, []), (2, [])])

    def test_tuples_with_empty_elements(self):
        self.assertEqual(group_tuples([(1, None), (2, None)]), [(1, []), (2, [])])

    def test_tuples_with_negative_elements(self):
        self.assertEqual(group_tuples([(-1, 2), (0, 3), (-1, -2)]), [(-1, [2, -2]), (0, [3])])

    def test_keyerror_when_grouping(self):
        with self.assertRaises(KeyError):
            group_tuples([(1, 2, 3), (4,)])
