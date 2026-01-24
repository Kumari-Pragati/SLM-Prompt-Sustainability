import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(group_tuples([(1, 2), (1, 3), (2, 4), (2, 5)]), [(1, 2, 3), (2, 4, 5)])
        self.assertListEqual(group_tuples([(1,), (2,), (3,)]), [(1), (2,), (3)])

    def test_edge_cases(self):
        self.assertListEqual(group_tuples([(1,), (1, 2)]), [(1,), (1, 2)])
        self.assertListEqual(group_tuples([(1,), (2, 3)]), [(1), (2, 3)])
        self.assertListEqual(group_tuples([(1, 2), (1,)]), [(1, 2), (1)])
        self.assertListEqual(group_tuples([(1,), (1, 2), (1, 3)]), [(1), (1, 2), (1, 3)])

    def test_complex(self):
        self.assertListEqual(group_tuples([(1, 2), (1, 3), (2, 4), (2, 5), (1, 6)]), [(1, 2, 3), (2, 4, 5), (1, 6)])
        self.assertListEqual(group_tuples([(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]), [(1), (2,), (3), (1, 2), (1, 3), (2, 3)])
