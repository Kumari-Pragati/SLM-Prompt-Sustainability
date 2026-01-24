import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_remove_odd_empty_list(self):
        self.assertEqual(remove_odd([]), [])

    def test_remove_odd_single_element(self):
        self.assertEqual(remove_odd([1]), [])

    def test_remove_odd_multiple_elements(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5]), [2, 4])

    def test_remove_odd_no_odd_numbers(self):
        self.assertEqual(remove_odd([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

    def test_remove_odd_all_odd_numbers(self):
        self.assertEqual(remove_odd([1, 3, 5, 7, 9]), [])

    def test_remove_odd_mixed_numbers(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]), [2, 4, 6, 8])
