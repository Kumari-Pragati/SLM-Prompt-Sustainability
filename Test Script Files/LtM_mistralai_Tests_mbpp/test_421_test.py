import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_single_element(self):
        self.assertEqual(concatenate_tuple((1,)), '1')
        self.assertEqual(concatenate_tuple((1,)), '1')

    def test_empty_input(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_negative_numbers(self):
        self.assertEqual(concatenate_tuple((-1, 0, 1)), '-1-0-1')

    def test_mixed_types(self):
        self.assertEqual(concatenate_tuple((1, 'a', 3.14)), '1-a-3.14')

    def test_long_input(self):
        self.assertEqual(concatenate_tuple((1000, 2000, 3000)), '1000-2000-3000')
