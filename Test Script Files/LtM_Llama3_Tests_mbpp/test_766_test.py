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

    def test_list_with_duplicates(self):
        self.assertEqual(pair_wise([1, 2, 2, 3]), [(1, 2), (2, 3)])

    def test_list_with_negative_numbers(self):
        self.assertEqual(pair_wise([-1, 0, 1]), [(-1, 0), (0, 1)])

    def test_list_with_floating_point_numbers(self):
        self.assertEqual(pair_wise([1.0, 2.0, 3.0]), [(1.0, 2.0), (2.0, 3.0)])
