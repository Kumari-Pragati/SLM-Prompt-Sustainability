import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):

    def test_empty_list_length_zero(self):
        self.assertEqual(empty_list(0), [])

    def test_empty_list_length_one(self):
        self.assertEqual(empty_list(1), [{},])

    def test_empty_list_length_five(self):
        self.assertEqual(len(empty_list(5)), 5)

    def test_empty_list_length_negative(self):
        with self.assertRaises(ValueError):
            empty_list(-1)

    def test_empty_list_length_non_integer(self):
        with self.assertRaises(TypeError):
            empty_list('a')
