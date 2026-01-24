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

    def test_large_tuple(self):
        self.assertEqual(remove_tuple(tuple(range(1, 101))), tuple(range(1, 101)))

    def test_large_duplicate_tuple(self):
        self.assertEqual(remove_tuple(tuple(range(1, 101)) + (1, 1, 1, 1)), tuple(range(1, 101)) + (1,))

    def test_mixed_types(self):
        self.assertEqual(remove_tuple((1, 'a', 'a', 2)), (1, 'a', 2))

    def test_negative_numbers(self):
        self.assertEqual(remove_tuple((-1, -1, 0, 0, 1, 1)), (-1, 0, 1))
