import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):

    def test_group_tuples(self):
        self.assertEqual(group_tuples([('a', 1), ('b', 2), ('a', 3)]), [('a', 1, 3), ('b', 2)])
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('y', 'a')]), [('x', 'y', 'z'), ('y', 'a')])
        self.assertEqual(group_tuples([('1', 2), ('2', 3), ('1', 4)]), [('1', 2, 4), ('2', 3)])
        self.assertEqual(group_tuples([]), [])
        self.assertEqual(group_tuples([('a', 1), ('a', 2), ('a', 3)]), [('a', 1, 2, 3)])
