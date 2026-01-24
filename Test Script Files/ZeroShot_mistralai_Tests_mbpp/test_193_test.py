import unittest
from mbpp_193_code import Tuple

from _193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(remove_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_duplicate_elements_in_tuple(self):
        self.assertEqual(remove_tuple((1, 1, 2, 2, 3)), (1, 2, 3))

    def test_mixed_elements_in_tuple(self):
        self.assertEqual(remove_tuple((1, 'a', 1, 'a', 2)), (1, 'a', 2))

    def test_tuple_with_none(self):
        self.assertEqual(remove_tuple((None, 1, 'a')), (None, 1, 'a'))
