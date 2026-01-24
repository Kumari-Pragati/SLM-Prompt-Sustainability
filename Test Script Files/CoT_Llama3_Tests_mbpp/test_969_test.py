import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(join_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(join_tuples([((1, 2),)]), [(1, 2)])

    def test_multiple_tuples(self):
        self.assertEqual(join_tuples([((1, 2), (1, 3)), ((1, 4),)]), [(1, 2, 3), (1, 4)])

    def test_consecutive_duplicates(self):
        self.assertEqual(join_tuples([((1, 2), (1, 3), (1, 4))]), [(1, 2, 3, 4)])

    def test_non_consecutive_duplicates(self):
        self.assertEqual(join_tuples([((1, 2), (2, 3), (1, 4)])), [(1, 2), (2, 3), (1, 4)])

    def test_empty_tuples(self):
        self.assertEqual(join_tuples([((),), ()]), [])

    def test_mixed_types(self):
        self.assertEqual(join_tuples([((1, 2), (3, 'a'), (4, 5.0)])), [(1, 2), 3, 'a', 4, 5.0])
