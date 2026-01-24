import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove_odd([]), [])

    def test_single_element(self):
        self.assertListEqual(remove_odd([1]), [])
        self.assertListEqual(remove_odd([2]), [2])

    def test_even_elements(self):
        self.assertListEqual(remove_odd([0, 2, 4, 6]), [0, 2, 4])
        self.assertListEqual(remove_odd([1, 3, 5, 7]), [])

    def test_odd_elements(self):
        self.assertListEqual(remove_odd([1, 3, 5, 7, 9]), [9])
        self.assertListEqual(remove_odd([1, 3, 5, 7, 9, 11]), [11])
