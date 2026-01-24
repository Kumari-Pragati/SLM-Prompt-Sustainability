import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])

    def test_single_element(self):
        self.assertEqual(pair_wise([1]), [])

    def test_empty_list(self):
        self.assertEqual(pair_wise([]), [])

    def test_negative_numbers(self):
        self.assertEqual(pair_wise([-1, -2, -3, -4]), [(-1, -2), (-2, -3), (-3, -4)])

    def test_zero(self):
        self.assertEqual(pair_wise([0, 1, 2, 3]), [(0, 1), (1, 2), (2, 3)])
