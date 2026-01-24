import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(remove_tuple(()), ())

    def test_single_element_input(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_multiple_elements_input(self):
        self.assertEqual(remove_tuple((1, 2, 3)), (1, 2, 3))

    def test_duplicates_input(self):
        self.assertEqual(remove_tuple((1, 1, 2, 2, 3)), (1, 2, 3))

    def test_empty_input_with_duplicates(self):
        self.assertEqual(remove_tuple(()), ())

    def test_empty_input_with_duplicates_and_single_element(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_empty_input_with_duplicates_and_multiple_elements(self):
        self.assertEqual(remove_tuple((1, 2, 2, 3)), (1, 2, 3))

    def test_empty_input_with_duplicates_and_multiple_elements_and_duplicates(self):
        self.assertEqual(remove_tuple((1, 1, 2, 2, 2, 3)), (1, 2, 3))
