import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):

    def test_pair_wise_empty_list(self):
        self.assertEqual(pair_wise([]), [])

    def test_pair_wise_single_element_list(self):
        self.assertEqual(pair_wise([1]), [])

    def test_pair_wise_two_elements_list(self):
        self.assertEqual(pair_wise([1, 2]), [(1, 2)])

    def test_pair_wise_three_elements_list(self):
        self.assertEqual(pair_wise([1, 2, 3]), [(1, 2), (2, 3)])

    def test_pair_wise_list_with_duplicates(self):
        self.assertEqual(pair_wise([1, 2, 2, 3, 3, 3]), [(1, 2), (2, 3), (3, 3)])

    def test_pair_wise_list_with_duplicates_and_empty(self):
        self.assertEqual(pair_wise([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 9, 9, 10, 11, 11, 11, 12, 13, 13, 13, 14, 15, 15, 15, 16, 17, 17, 17, 18, 19, 19, 19, 20, 21, 21, 21, 22, 23, 23, 23, 24, 25, 25, 25, 26, 27, 27, 27, 28, 29, 29, 29, 30]), [])
