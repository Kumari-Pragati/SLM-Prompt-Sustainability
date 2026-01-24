import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(join_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(join_tuples([(1, 2, 3)]), [(1, 2, 3)])

    def test_multiple_tuples_same_first_element(self):
        self.assertEqual(join_tuples([(1, 2), (1, 3), (1, 4)]), [(1, 2), (1, 3, 4)])

    def test_multiple_tuples_different_first_element(self):
        self.assertEqual(join_tuples([(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])

    def test_mixed_tuples_same_first_element(self):
        self.assertEqual(join_tuples([(1, 2), (1, 3), (1,), (1, 5)]), [(1, 2), (1, 3, 5)])

    def test_mixed_tuples_different_first_element(self):
        self.assertEqual(join_tuples([(1, 2), (3, 4), (5,), (6,)]), [(1, 2), (3, 4), (5,), (6,)])

    def test_empty_sublist(self):
        self.assertEqual(join_tuples([(1, 2), (), (3, 4)]), [(1, 2), (3, 4)])

    def test_single_element_sublist(self):
        self.assertEqual(join_tuples([(1, 2), (3,), (4, 5)]), [(1, 2), (3,), (4, 5)])

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            join_tuples(-1)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            join_tuples(123)
