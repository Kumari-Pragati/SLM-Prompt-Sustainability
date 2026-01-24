import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):

    def test_all_tuples_have_same_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3), "All tuples have same length")

    def test_all_tuples_do_not_have_same_length(self):
        self.assertEqual(get_equal([(1, 2), (3, 4, 5), (6, 7)], 2), "All tuples do not have same length")

    def test_empty_input(self):
        self.assertEqual(get_equal([], 0), "All tuples have same length")

    def test_input_with_empty_tuples(self):
        self.assertEqual(get_equal([(), ()], 0), "All tuples have same length")

    def test_input_with_different_length_tuples(self):
        self.assertEqual(get_equal([(1, 2), (3, 4, 5)], 2), "All tuples do not have same length")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            get_equal("not a list", 2)

    def test_invalid_tuple_in_input(self):
        with self.assertRaises(TypeError):
            get_equal([(1, 2), "not a tuple", (3, 4)], 2)
