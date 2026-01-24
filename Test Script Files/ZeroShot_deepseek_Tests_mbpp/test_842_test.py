import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):

    def test_get_odd_occurence(self):
        self.assertEqual(get_odd_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13), 5)
        self.assertEqual(get_odd_occurence([10, 20, 10, 30, 20, 30, 40, 40, 40], 9), 10)
        self.assertEqual(get_odd_occurence([1, 2, 3, 2, 1], 5), 3)
        self.assertEqual(get_odd_occurence([1, 1, 2, 2, 1, 1, 2, 2, 13, 13], 10), 13)
        self.assertEqual(get_odd_occurence([1], 1), 1)
