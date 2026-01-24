import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(join_tuples([([1, 2], [3, 4]), ([5, 6], [7, 8])]), [([1, 2, 3, 4],), ([5, 6, 7, 8],)])

    def test_edge_input(self):
        self.assertListEqual(join_tuples([([1, 2],), ([3, 4],), ([5, 6],)]), [([1, 2],), ([3, 4],), ([5, 6],)])
        self.assertListEqual(join_tuples([([1, 2],), ([],), ([5, 6],)]), [([1, 2],), ([],), ([5, 6],)])
        self.assertListEqual(join_tuples([([],), ([1, 2],), ([3, 4],)]), [([],), ([1, 2],), ([3, 4],)])

    def test_boundary_input(self):
        self.assertListEqual(join_tuples([([],)]), [([],)])
        self.assertListEqual(join_tuples([([1],)]), [([1],)])
        self.assertListEqual(join_tuples([([1], [2])]],), [([1],), ([2],)])

    def test_special_input(self):
        self.assertListEqual(join_tuples([([1, 2], [3]), ([4, 5], [6])]],), [([1, 2, 3],), ([4, 5, 6],)])
        self.assertListEqual(join_tuples([([1, 2], [3, 4]), ([5], [6])]],), [([1, 2, 3],), ([5], [6])])
