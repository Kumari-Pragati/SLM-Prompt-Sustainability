import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(group_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(group_tuples([(1, 2)]), [(1, 2)])

    def test_multiple_tuples_same_first_element(self):
        self.assertEqual(group_tuples([(1, 2), (1, 3), (1, 4)]), [(1, [2, 3, 4])])

    def test_multiple_tuples_different_first_element(self):
        self.assertEqual(group_tuples([(1, 2), (3, 4)]), [(1, [2]), (3, [4])])

    def test_keyerror_handling(self):
        self.assertEqual(group_tuples([(1,), (2, 3)]), [(1, [2, 3])])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            group_tuples("not a list")

    def test_invalid_input_element(self):
        with self.assertRaises(TypeError):
            group_tuples([(1, 2), (1, "not a number")])
