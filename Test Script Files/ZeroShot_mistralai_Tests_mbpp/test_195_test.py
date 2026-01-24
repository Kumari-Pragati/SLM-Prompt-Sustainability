import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(first([], 5, 0), -1)

    def test_single_element(self):
        self.assertEqual(first([1], 1, 0), 0)
        self.assertEqual(first([1], 2, 0), -1)

    def test_element_not_found(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 6, 5), -1)

    def test_element_found_at_beginning(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 1, 0), 0)

    def test_element_found_in_middle(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 3, 4), 2)

    def test_element_found_at_end(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 5, 4), 4)
