import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_remove_tuples(self):
        self.assertEqual(remove_tuples([(1, 2), (3, 4), (5, 6, 7)], 2), [(1, 2), (3, 4)])
        self.assertEqual(remove_tuples([(1, 2, 3), (4, 5), (6,)], 3), [(1, 2, 3), (6,)])
        self.assertEqual(remove_tuples([], 2), [])
        self.assertEqual(remove_tuples([(1, 2), (3, 4), (5, 6, 7)], 3), [(1, 2), (3, 4), (5, 6, 7)])
        self.assertEqual(remove_tuples([(1, 2, 3), (4, 5, 6), (7,)], 1), [])
