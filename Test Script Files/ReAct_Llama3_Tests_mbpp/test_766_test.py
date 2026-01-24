import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(pair_wise([]), [])

    def test_single_element_list(self):
        self.assertEqual(pair_wise([1]), [])

    def test_two_element_list(self):
        self.assertEqual(pair_wise([1, 2]), [(1, 2)])

    def test_three_element_list(self):
        self.assertEqual(pair_wise([1, 2, 3]), [(1, 2), (2, 3)])

    def test_large_list(self):
        self.assertEqual(pair_wise([1, 2, 3, 4, 5]), [(1, 2), (2, 3), (3, 4), (4, 5)])

    def test_list_with_duplicates(self):
        self.assertEqual(pair_wise([1, 2, 2, 3, 3, 3]), [(1, 2), (2, 2), (2, 3), (3, 3)])
