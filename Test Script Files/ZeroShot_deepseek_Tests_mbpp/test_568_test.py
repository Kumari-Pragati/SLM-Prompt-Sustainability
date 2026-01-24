import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):

    def test_empty_list_with_zero_length(self):
        self.assertEqual(empty_list(0), [])

    def test_empty_list_with_positive_length(self):
        self.assertEqual(len(empty_list(5)), 5)
        self.assertEqual(empty_list(5), [{}]*5)

    def test_empty_list_with_negative_length(self):
        self.assertEqual(empty_list(-5), [])

    def test_empty_list_with_non_integer_length(self):
        self.assertEqual(empty_list(3.5), [{}]*3)
