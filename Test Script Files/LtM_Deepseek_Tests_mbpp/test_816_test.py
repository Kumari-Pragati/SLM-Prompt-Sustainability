import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):

    def test_simple_tuple(self):
        self.assertEqual(clear_tuple(('a', 'b', 'c')), ())

    def test_empty_tuple(self):
        self.assertEqual(clear_tuple(()), ())

    def test_tuple_with_one_element(self):
        self.assertEqual(clear_tuple(('single',)), ())

    def test_tuple_with_duplicate_elements(self):
        self.assertEqual(clear_tuple(('duplicate', 'duplicate')), ())

    def test_tuple_with_large_number_of_elements(self):
        self.assertEqual(clear_tuple(('a', 'b', 'c', 'd', 'e')), ())
