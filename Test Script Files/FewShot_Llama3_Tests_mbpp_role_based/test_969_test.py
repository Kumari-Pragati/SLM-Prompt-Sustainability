import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(join_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(join_tuples([(1, 2, 3)]), [(1, 2, 3)])

    def test_multiple_tuples(self):
        self.assertEqual(join_tuples([(1, 2, 3), (1, 4, 5), (2, 6, 7)]), [(1, 2, 3, 4, 5), (2, 6, 7)])

    def test_tuples_with_common_key(self):
        self.assertEqual(join_tuples([(1, 2, 3), (1, 4, 5), (1, 6, 7)]), [(1, 2, 3, 4, 5, 6, 7)])

    def test_tuples_with_no_common_key(self):
        self.assertEqual(join_tuples([(1, 2, 3), (2, 4, 5), (3, 6, 7)]), [(1, 2, 3), (2, 4, 5), (3, 6, 7)])

    def test_tuples_with_empty_sublist(self):
        self.assertEqual(join_tuples([(1, 2, 3), (1, 4, 5, []), (2, 6, 7)]), [(1, 2, 3, 4, 5), (2, 6, 7)])
