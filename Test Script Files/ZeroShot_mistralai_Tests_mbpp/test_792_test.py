import unittest
from792_code import count_list

class TestCountList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count_list([1, 2, 3]), 3)

    def test_list_with_duplicates(self):
        self.assertEqual(count_list([1, 1, 2, 2, 3]), 3)

    def test_list_with_non_integer_elements(self):
        self.assertEqual(count_list([1, 'a', 2]), 3)
