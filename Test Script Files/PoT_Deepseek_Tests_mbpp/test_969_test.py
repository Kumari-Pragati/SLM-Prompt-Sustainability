import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(join_tuples([(1, 2), (1, 3), (2, 4)]), [(1, 2, 3), (2, 4)])

    def test_edge_case(self):
        self.assertEqual(join_tuples([(1, 2), (1,)]), [(1, 2), (1,)])

    def test_boundary_case(self):
        self.assertEqual(join_tuples([(1, 2), (1, 2)]), [(1, 2, 2)])

    def test_corner_case(self):
        self.assertEqual(join_tuples([(1, 2), (3, 4), (1, 2)]), [(1, 2, 2), (3, 4)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            join_tuples([1, 2, 3])
