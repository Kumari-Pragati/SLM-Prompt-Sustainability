import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_tuplex([], 1), 0)

    def test_single_element(self):
        self.assertEqual(count_tuplex([(1, 2)], 1), 1)

    def test_multiple_elements(self):
        self.assertEqual(count_tuplex([(1, 2), (1, 3), (2, 3)], 1), 2)

    def test_value_not_in_list(self):
        self.assertEqual(count_tuplex([(1, 2), (1, 3), (2, 3)], 4), 0)

    def test_value_in_multiple_tuples(self):
        self.assertEqual(count_tuplex([(1, 2), (1, 3), (2, 3), (1, 2)], 1), 2)

    def test_value_in_single_tuple(self):
        self.assertEqual(count_tuplex([(1, 2)], (1, 2)), 1)

    def test_value_in_list_with_duplicates(self):
        self.assertEqual(count_tuplex([(1, 2), (1, 2), (1, 3)], 1), 2)

    def test_value_in_list_with_none_type(self):
        self.assertRaises(TypeError, count_tuplex, [(1, 2), (1, 3), (2, 3)], None)

    def test_value_in_list_with_string_type(self):
        self.assertRaises(TypeError, count_tuplex, [(1, 2), (1, 3), (2, 3)], "string")
