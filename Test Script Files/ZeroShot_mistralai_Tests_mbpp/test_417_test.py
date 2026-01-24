import unittest
from mbpp_417_code import group_tuples

class TestGroupTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(group_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(group_tuples([(1, 2)]), [(1, 2)])

    def test_multiple_tuples_same_first_element(self):
        self.assertEqual(group_tuples([(1, 2), (1, 3), (1, 4)]), [(1, [2, 3, 4])])

    def test_multiple_tuples_different_first_elements(self):
        self.assertEqual(group_tuples([(1, 2), (3, 4), (1, 5)]), [(1, [2]), (3, [4]), (1, [5])])

    def test_keyerror_exception(self):
        self.assertEqual(group_tuples([(1,), (2, 3)]), [(1, [2, 3])])
