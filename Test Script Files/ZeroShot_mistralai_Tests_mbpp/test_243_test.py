import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_single_element(self):
        self.assertEqual(sort_on_occurence([(1, 1)]), [(1, 1, 1, 1)])

    def test_duplicate_elements(self):
        self.assertEqual(sort_on_occurence([(1, 1), (1, 2), (2, 1), (2, 2)]), [(1, 1, 2, 2), (2, 1, 2, 1)])

    def test_unique_elements(self):
        self.assertEqual(sort_on_occurence([(1, 1), (2, 2), (3, 3)]), [(1, 1, 1, 1), (2, 2, 1, 1), (3, 3, 1, 1)])

    def test_mixed_elements(self):
        self.assertEqual(sort_on_occurence([(1, 1), (2, 2), (1, 2), (2, 1)]), [(1, 1, 2, 2), (2, 1, 2, 1)])
