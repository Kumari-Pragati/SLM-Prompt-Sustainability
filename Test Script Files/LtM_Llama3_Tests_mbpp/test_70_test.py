import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(get_equal([(1,2,3), (4,5,6)], 3), "All tuples have same length")

    def test_empty_input(self):
        self.assertEqual(get_equal([], 3), "All tuples do not have same length")

    def test_single_tuple_input(self):
        self.assertEqual(get_equal([(1,2,3)], 3), "All tuples have same length")

    def test_tuple_length_mismatch(self):
        self.assertEqual(get_equal([(1,2,3), (1,2)], 3), "All tuples do not have same length")

    def test_tuple_length_mismatch2(self):
        self.assertEqual(get_equal([(1,2,3), (1,2,3,4)], 3), "All tuples do not have same length")

    def test_tuple_length_mismatch3(self):
        self.assertEqual(get_equal([(1,2,3), (1,2,3,4,5)], 3), "All tuples do not have same length")
