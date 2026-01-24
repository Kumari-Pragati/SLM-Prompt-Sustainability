import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(group_tuples([(1, 2), (1, 3), (2, 4), (2, 5)]), [(1, 2, 3), (2, 4, 5)])
        self.assertListEqual(group_tuples([(1,), (2, 3), (4, 5)]), [(1), (2, 3), (4, 5)])
        self.assertListEqual(group_tuples([(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])

    def test_edge_input(self):
        self.assertListEqual(group_tuples([(1,), (1,), (2,)]), [(1), (1, 2)])
        self.assertListEqual(group_tuples([(1,), (1,), (1,)]), [(1), (1,), (1)])
        self.assertListEqual(group_tuples([(1,), (1, 2), (1, 3)]), [(1), (1, 2), (1, 3)])

    def test_invalid_input(self):
        self.assertRaises(TypeError, group_tuples, [1, 2])
        self.assertRaises(TypeError, group_tuples, [(1, 2, 3), "a"])
        self.assertRaises(TypeError, group_tuples, [(1,), [2, 3]])
