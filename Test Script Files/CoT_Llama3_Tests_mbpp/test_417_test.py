import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(group_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(group_tuples([(1,)]), [(1,)])

    def test_multiple_tuples(self):
        self.assertEqual(group_tuples([(1, 2), (1, 3), (2, 4)]), [(1, 2, 3), (2, 4)])

    def test_empty_tuples(self):
        self.assertEqual(group_tuples([]), [])

    def test_key_error(self):
        self.assertEqual(group_tuples([(1, 2), (3, 4)]), [(1, 2), (3, 4)])

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            group_tuples([1, 2, 3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            group_tuples("hello")
