import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(join_tuples([([1],), ([2],), ([3],)]), [([1], (2,)), ([2], (3,))])
        self.assertListEqual(join_tuples([([1],), ([2], [3]), ([4],)]), [([1], (2, 3)), ([2, 3], (4,))])

    def test_edge_cases(self):
        self.assertListEqual(join_tuples([([1],), ([],)]), [([1],)])
        self.assertListEqual(join_tuples([([1],), ([2, 3],)]), [([1],), ([2, 3],)])
        self.assertListEqual(join_tuples([([1],), ([2], [3]), ([],)]), [([1],), ([2], [3])])
        self.assertListEqual(join_tuples([([1],), ([], [3]), ([2],)]), [([1],), ([], [3]), ([2],)])

    def test_complex(self):
        self.assertListEqual(join_tuples([([1],), ([2], [3]), ([4], [5]), ([6],)]), [([1], (2, 3)), ([2, 3], (4, 5)), ([4, 5], (6,))])
        self.assertListEqual(join_tuples([([1],), ([2], [3]), ([4], [5, 6]), ([7],)]), [([1], (2, 3)), ([2, 3], (4, 5, 6)), ([4, 5, 6], (7,))])
        self.assertListEqual(join_tuples([([1],), ([], [3]), ([2], [4]), ([],)]), [([1],), ([], [3]), ([2], [4])])
        self.assertListEqual(join_tuples([([1],), ([2],), ([], [3]), ([4],)]), [([1], (2,)), ([], [3]), ([4],)])
