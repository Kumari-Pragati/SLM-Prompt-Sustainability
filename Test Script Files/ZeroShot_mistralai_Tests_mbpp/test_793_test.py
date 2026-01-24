import unittest
from793_code import last

class TestLastFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(last([], 5, 0), -1)

    def test_single_element(self):
        self.assertEqual(last([5], 5, 0), 0)
        self.assertEqual(last([5], 3, 0), -1)

    def test_multiple_elements(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 4), 4)
        self.assertEqual(last([1, 2, 3, 4, 5], 3, 4), 2)
        self.assertEqual(last([1, 2, 3, 4, 5], 6, 4), -1)

    def test_duplicates(self):
        self.assertEqual(last([1, 1, 2, 3, 4, 4, 5], 4, 6), 5)
        self.assertEqual(last([1, 1, 2, 3, 4, 4, 5], 3, 6), 3)
        self.assertEqual(last([1, 1, 2, 3, 4, 4, 5], 6, 6), -1)
