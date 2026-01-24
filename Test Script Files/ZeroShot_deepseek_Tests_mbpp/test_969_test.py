import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(join_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(join_tuples([(1, 2, 3)]), [(1, 2, 3)])

    def test_multiple_tuples(self):
        self.assertEqual(join_tuples([(1, 2, 3), (1, 4, 5), (2, 6, 7)]), [(1, 2, 3, 4, 5), (2, 6, 7)])

    def test_different_start_tuples(self):
        self.assertEqual(join_tuples([(1, 2, 3), (2, 4, 5)]), [(1, 2, 3), (2, 4, 5)])

    def test_nested_tuples(self):
        self.assertEqual(join_tuples([(1, (2, 3)), (1, (4, 5))]), [(1, (2, 3, 4, 5))])
