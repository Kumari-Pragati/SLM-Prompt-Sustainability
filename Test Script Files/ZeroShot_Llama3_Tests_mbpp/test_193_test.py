import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_remove_tuple(self):
        self.assertEqual(remove_tuple((1, 2, 3, 2, 1)), (1, 2, 3))
        self.assertEqual(remove_tuple((1, 1, 2, 2, 3, 3)), (1, 2, 3))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_tuple(()), ())
        self.assertEqual(remove_tuple((1,)), (1,))
        self.assertEqual(remove_tuple((1, 1)), (1,))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_remove_tuple_empty(self):
        self.assertEqual(remove_tuple(()), ())

    def test_remove_tuple_single_element(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_remove_tuple_duplicates(self):
        self.assertEqual(remove_tuple((1, 1, 2, 2, 3, 3)), (1, 2, 3))
