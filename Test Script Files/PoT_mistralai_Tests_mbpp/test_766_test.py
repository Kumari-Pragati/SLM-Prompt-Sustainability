import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(pair_wise([1, 2, 3, 4, 5]), [(1, 2), (2, 3), (3, 4), (4, 5)])

    def test_edge_case_single_element(self):
        self.assertEqual(pair_wise([1]), [(1, None)])

    def test_edge_case_empty_list(self):
        self.assertEqual(pair_wise([]), [])

    def test_edge_case_two_elements(self):
        self.assertEqual(pair_wise([1, 2]), [(1, 2)])

    def test_boundary_case_first_element(self):
        self.assertEqual(pair_wise([1]), [(1, None)])

    def test_boundary_case_last_element(self):
        self.assertEqual(pair_wise([1, 2]), [(1, 2)])
