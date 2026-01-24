import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):

    def test_pair_wise(self):
        self.assertEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])
        self.assertEqual(pair_wise([5, 6, 7, 8, 9]), [(5, 6), (6, 7), (7, 8), (8, 9)])
        self.assertEqual(pair_wise([10, 11, 12]), [(10, 11), (11, 12)])
        self.assertEqual(pair_wise([1]), [])
        self.assertEqual(pair_wise([]), [])

    def test_pair_wise_empty_list(self):
        self.assertEqual(pair_wise([]), [])

    def test_pair_wise_single_element(self):
        self.assertEqual(pair_wise([1]), [])
