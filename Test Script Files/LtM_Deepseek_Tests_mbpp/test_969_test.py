import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(join_tuples([(1, 2), (1, 3), (2, 4)]), [(1, 2, 3), (2, 4)])

    def test_edge_conditions(self):
        self.assertEqual(join_tuples([]), [])
        self.assertEqual(join_tuples([(1, 2)]), [(1, 2)])

    def test_complex_cases(self):
        self.assertEqual(join_tuples([(1, 2), (1, 3), (1, 4)]), [(1, 2, 3, 4)])
        self.assertEqual(join_tuples([(1, 2), (2, 3), (3, 4)]), [(1, 2), (2, 3), (3, 4)])
