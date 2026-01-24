import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):

    def test_empty_list(self):
        """Test pair_wise on an empty list"""
        self.assertListEqual(pair_wise([]), [])

    def test_single_element_list(self):
        """Test pair_wise on a list with a single element"""
        self.assertListEqual(pair_wise([1]), [(1, None)])

    def test_normal_list(self):
        """Test pair_wise on a normal list"""
        self.assertListEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])

    def test_list_with_last_element(self):
        """Test pair_wise on a list with the last element"""
        self.assertListEqual(pair_wise([1, 2, 3]), [(1, 2), (2, 3)])

    def test_list_with_negative_numbers(self):
        """Test pair_wise on a list with negative numbers"""
        self.assertListEqual(pair_wise([-1, 0, 1]), [(-1, 0), (0, 1)])

    def test_list_with_duplicates(self):
        """Test pair_wise on a list with duplicates"""
        self.assertListEqual(pair_wise([1, 1, 2, 2, 3]), [(1, 1), (1, 2), (2, 2), (2, 3)])
