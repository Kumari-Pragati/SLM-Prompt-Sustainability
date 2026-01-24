import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(pair_wise([]), [])

    def test_single_element_list(self):
        self.assertListEqual(pair_wise([1]), [(1, None)])

    def test_two_elements_list(self):
        self.assertListEqual(pair_wise([1, 2]), [(1, 2)])

    def test_three_elements_list(self):
        self.assertListEqual(pair_wise([1, 2, 3]), [(1, 2), (2, 3)])

    def test_four_elements_list(self):
        self.assertListEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])

    def test_list_with_none(self):
        self.assertListEqual(pair_wise([1, None, 3]), [(1, None), (None, 3)])
