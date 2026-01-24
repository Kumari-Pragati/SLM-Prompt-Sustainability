import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_tuples([], 0), [])

    def test_single_element_list(self):
        self.assertEqual(remove_tuples([1], 1), [])

    def test_single_tuple_list(self):
        self.assertEqual(remove_tuples([(1,)], 1), [])

    def test_multiple_elements_list(self):
        self.assertEqual(remove_tuples([1, 2, 3], 0), [1, 2, 3])

    def test_multiple_tuples_list(self):
        self.assertEqual(remove_tuples([(1, 2), (3, 4), (5, 6)], 2), [])

    def test_mixed_list(self):
        self.assertEqual(remove_tuples([1, (2, 3), 4, 5], 2), [1, 4, 5])

    def test_non_integer_K(self):
        with self.assertRaises(TypeError):
            remove_tuples([1, 2, 3], 'a')

    def test_negative_K(self):
        with self.assertRaises(TypeError):
            remove_tuples([1, 2, 3], -1)
