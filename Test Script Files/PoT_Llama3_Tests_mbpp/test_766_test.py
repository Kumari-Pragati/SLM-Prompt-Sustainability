import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])

    def test_edge_case_empty_list(self):
        self.assertEqual(pair_wise([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(pair_wise([1]), [])

    def test_edge_case_two_element_list(self):
        self.assertEqual(pair_wise([1, 2]), [(1, 2)])

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(pair_wise([1, 2, 2, 3, 3, 3]), [(1, 2), (2, 3), (3, 3)])

    def test_edge_case_list_with_duplicates_and_empty(self):
        self.assertEqual(pair_wise([1, 2, 2, 3, 3, 3, 4]), [(1, 2), (2, 3), (3, 3), (3, 4)])
