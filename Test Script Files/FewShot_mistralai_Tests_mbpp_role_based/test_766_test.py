import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):
    def test_pair_wise_with_two_elements(self):
        self.assertEqual(pair_wise([1, 2]), [(1, 2)])

    def test_pair_wise_with_three_elements(self):
        self.assertEqual(pair_wise([1, 2, 3]), [(1, 2), (2, 3)])

    def test_pair_wise_with_four_elements(self):
        self.assertEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])

    def test_pair_wise_with_empty_list(self):
        self.assertEqual(pair_wise([]), [])

    def test_pair_wise_with_single_element(self):
        self.assertEqual(pair_wise([1]), [])
