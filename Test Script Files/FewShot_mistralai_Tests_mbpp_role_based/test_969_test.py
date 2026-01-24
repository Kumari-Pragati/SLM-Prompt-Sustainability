import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(join_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(join_tuples([(1, 2, 3)]), [(1, 2, 3)])

    def test_multiple_tuples_same_first_element(self):
        self.assertEqual(join_tuples([(1, 2), (1, 3), (1, 4)]), [(1, 2, 3, 4)])

    def test_multiple_tuples_different_first_element(self):
        self.assertEqual(join_tuples([(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])

    def test_tuples_with_empty_sublists(self):
        self.assertEqual(join_tuples([(1,), (2, 3), (4,)]), [(1,), (2, 3), (4,)])

    def test_tuples_with_mixed_types(self):
        with self.assertRaises(TypeError):
            join_tuples([(1, 2), (3, 'a'), (4, 5)])
