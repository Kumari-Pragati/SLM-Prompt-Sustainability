import unittest
from mbpp_237_code import Counter
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(check_occurences([]), {})

    def test_single_element(self):
        self.assertEqual(check_occurences([[1]]), {(1,): 1})

    def test_multiple_elements(self):
        self.assertEqual(check_occurences([[1, 2], [2, 1]]), {(1, 2): 1, (2, 1): 1})

    def test_duplicates(self):
        self.assertEqual(check_occurences([[1, 2], [1, 2]]), {(1, 2): 2})

    def test_unsorted_elements(self):
        self.assertEqual(check_occurences([[2, 1], [1, 2]]]), {(1, 2): 2})
