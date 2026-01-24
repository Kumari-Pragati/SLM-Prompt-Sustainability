import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(join_tuples([([1, 2],), ([3, 4],), ([5, 6],)]), [(1, 2), (3, 4), (5, 6)])

    def test_edge_case(self):
        self.assertEqual(join_tuples([([1, 2],), ([1, 3],), ([2, 4],)]), [(1, 2, 3), (2, 4)])

    def test_edge_case2(self):
        self.assertEqual(join_tuples([([1, 2],), ([1, 2],), ([3, 4],)]), [(1, 2), (3, 4)])

    def test_edge_case3(self):
        self.assertEqual(join_tuples([]), [])

    def test_edge_case4(self):
        self.assertEqual(join_tuples([([1, 2],)]), [(1, 2)])

    def test_edge_case5(self):
        self.assertEqual(join_tuples([([1, 2],), ([3, 4],), ([5, 6],), ([7, 8],)]), [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_edge_case6(self):
        self.assertEqual(join_tuples([([1, 2],), ([1, 2],), ([3, 4],), ([3, 4],)]), [(1, 2), (3, 4)])

    def test_edge_case7(self):
        self.assertEqual(join_tuples([([1, 2],), ([1, 2, 3],)]), [(1, 2), (1, 2, 3)])

    def test_edge_case8(self):
        self.assertEqual(join_tuples([([1, 2],), ([1, 2, 3],), ([4, 5],)]), [(1, 2), (1, 2, 3), (4, 5)])
