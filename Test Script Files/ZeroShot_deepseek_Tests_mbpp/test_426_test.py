import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):

    def test_filter_oddnumbers(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(filter_oddnumbers([10, 20, 30, 40, 50]), [])
        self.assertEqual(filter_oddnumbers([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(filter_oddnumbers([]), [])
        self.assertEqual(filter_oddnumbers([2, 4, 6, 8]), [])
