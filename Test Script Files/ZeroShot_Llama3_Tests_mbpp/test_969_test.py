import unittest
from mbpp_969_code import join_tuples

class TestJoinTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(join_tuples([]), [])

    def test_single_tuple(self):
        self.assertEqual(join_tuples([(1, 2)]), [(1, 2)])

    def test_multiple_tuples(self):
        self.assertEqual(join_tuples([(1, 2), (1, 3), (2, 4)]), [(1, 2, 3), (2, 4)])

    def test_tuples_with_same_first_element(self):
        self.assertEqual(join_tuples([(1, 2), (1, 3), (1, 4)]), [(1, 2, 3, 4)])

    def test_tuples_with_same_first_element_and_diff_second_elements(self):
        self.assertEqual(join_tuples([(1, 2), (1, 3), (1, 4, 5)]), [(1, 2, 3, 4, 5)])

    def test_tuples_with_diff_first_elements(self):
        self.assertEqual(join_tuples([(1, 2), (2, 3), (3, 4)]), [(1, 2), (2, 3), (3, 4)])

    def test_tuples_with_diff_first_elements_and_diff_second_elements(self):
        self.assertEqual(join_tuples([(1, 2), (2, 3), (3, 4, 5)]), [(1, 2), (2, 3), (3, 4, 5)])
