import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(group_tuples([(1, 2), (1, 3), (2, 4)]), [
                         (1, 2, 3), (2, 4)])

    def test_empty_input(self):
        self.assertEqual(group_tuples([]), [])

    def test_single_tuple_input(self):
        self.assertEqual(group_tuples([(1, 2)]), [(1, 2)])

    def test_duplicate_keys(self):
        self.assertEqual(group_tuples([(1, 2), (1, 3)]), [(1, 2, 3)])

    def test_large_input(self):
        large_input = [(i, i+1) for i in range(1000)]
        self.assertEqual(group_tuples(large_input), large_input)

    def test_mixed_types(self):
        self.assertEqual(group_tuples([(1, 'a'), (1, 'b')]), [(1, 'a', 'b')])
