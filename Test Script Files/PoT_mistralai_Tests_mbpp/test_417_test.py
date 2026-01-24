import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(group_tuples([(1, 2), (1, 3), (2, 4), (2, 5)]), [( [1, 2], [3] ), ( [1, 2], [4, 5] )])
        self.assertEqual(group_tuples([(1, 2, 3), (1, 4), (2, 5), (2, 6)]), [( [1, 2, 3], [4] ), ( [1], [5, 6] ), ( [2], [5, 6] )])

    def test_edge_cases(self):
        self.assertEqual(group_tuples([(1), (2)]), [([1]), ([2])])
        self.assertEqual(group_tuples([(1,), (2,)]), [([1]), ([2])])
        self.assertEqual(group_tuples([(1,), (2)]), [([1]), ([2])])

    def test_corner_cases(self):
        self.assertEqual(group_tuples([]), [])
        self.assertEqual(group_tuples([(1)]), [([1])])
        self.assertEqual(group_tuples([(1, 2), (1, 2)]), [([1, 2], [])])
