import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_tuple((1, 2, 2, 3, 4, 4)), (1, 2, 3, 4))

    def test_empty_tuple(self):
        self.assertEqual(remove_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(remove_tuple((5,)), (5,))

    def test_duplicate_elements(self):
        self.assertEqual(remove_tuple((1, 1, 1, 1)), (1,))

    def test_string_elements(self):
        self.assertEqual(remove_tuple(('a', 'b', 'b', 'c')), ('a', 'b', 'c'))

    def test_mixed_elements(self):
        self.assertEqual(remove_tuple((1, 'a', 'a', 2)), (1, 'a', 2))

    def test_large_tuple(self):
        self.assertEqual(remove_tuple(tuple(range(1, 101)) + (1,)), tuple(range(1, 101)))

    def test_none_elements(self):
        self.assertEqual(remove_tuple((None, None, None)), (None,))

    def test_duplicate_none_elements(self):
        self.assertEqual(remove_tuple((None, None, None, None)), (None,))

    def test_mixed_none_elements(self):
        self.assertEqual(remove_tuple((1, None, None, 2)), (1, None, 2))
