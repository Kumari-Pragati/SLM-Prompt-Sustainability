import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_remove_tuple_with_duplicates(self):
        test_tup = (1, 2, 2, 3, 4, 4, 5, 6, 6, 7)
        expected_output = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(remove_tuple(test_tup), expected_output)

    def test_remove_tuple_with_no_duplicates(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7)
        expected_output = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(remove_tuple(test_tup), expected_output)

    def test_remove_tuple_with_empty_tup(self):
        test_tup = ()
        expected_output = ()
        self.assertEqual(remove_tuple(test_tup), expected_output)

    def test_remove_tuple_with_single_element(self):
        test_tup = (1,)
        expected_output = (1,)
        self.assertEqual(remove_tuple(test_tup), expected_output)
