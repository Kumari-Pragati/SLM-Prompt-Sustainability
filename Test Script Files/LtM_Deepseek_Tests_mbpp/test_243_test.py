import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sort_on_occurence([('a', 1), ('b', 2), ('a', 3)]), [('a', 1, 3), ('b', 2, 1)])

    def test_empty_input(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_single_element_input(self):
        self.assertEqual(sort_on_occurence([('a', 1)]), [('a', 1, 1)])

    def test_duplicate_elements(self):
        self.assertEqual(sort_on_occurence([('a', 1), ('a', 2)]), [('a', 1, 2)])

    def test_large_input(self):
        self.assertEqual(sort_on_occurence([('a', i) for i in range(1, 101)]), [('a', i, 1) for i in range(1, 101)])

    def test_negative_numbers(self):
        self.assertEqual(sort_on_occurence([('a', -1), ('b', -2), ('a', -3)]), [('a', -1, 3), ('b', -2, 1)])

    def test_large_numbers(self):
        self.assertEqual(sort_on_occurence([('a', 1000), ('b', 2000), ('a', 3000)]), [('a', 1000, 3), ('b', 2000, 1)])
