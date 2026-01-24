import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), ((2, 3),))

    def test_edge_case_empty(self):
        self.assertEqual(concatenate_elements(()), (()))

    def test_edge_case_single_element(self):
        self.assertEqual(concatenate_elements((1,)), ((1,),))

    def test_edge_case_two_elements(self):
        self.assertEqual(concatenate_elements((1, 2)), ((3,),))

    def test_edge_case_three_elements(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), ((2, 3),))

    def test_edge_case_four_elements(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4)), ((2, 3, 4),))

    def test_edge_case_five_elements(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5)), ((2, 3, 4, 5),))

    def test_edge_case_six_elements(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5, 6)), ((2, 3, 4, 5, 6),))
