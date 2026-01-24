import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_tuples([(4, 8, 12), (3, 6, 9)], 2), '[(4, 8, 12)]')

    def test_edge_case(self):
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6)], 1), '[(1, 2, 3), (4, 5, 6)]')

    def test_boundary_case(self):
        self.assertEqual(find_tuples([(0, 0, 0), (1, 2, 3)], 0), '[(0, 0, 0)]')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_tuples("not a list", 2)
