import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Seq_Linear([1, 3, 5, 7, 9]), "Linear Sequence")

    def test_edge_case_single_element(self):
        self.assertEqual(Seq_Linear([5]), "Linear Sequence")

    def test_edge_case_empty_sequence(self):
        self.assertEqual(Seq_Linear([]), "Non Linear Sequence")

    def test_boundary_case_two_elements(self):
        self.assertEqual(Seq_Linear([1, 2]), "Linear Sequence")

    def test_boundary_case_two_elements_reverse(self):
        self.assertEqual(Seq_Linear([2, 1]), "Non Linear Sequence")

    def test_corner_case_negative_numbers(self):
        self.assertEqual(Seq_Linear([-1, 0, 1, 2, 3]), "Linear Sequence")

    def test_corner_case_non_consecutive_sequence(self):
        self.assertEqual(Seq_Linear([1, 3, 5, 7, 9]), "Non Linear Sequence")

    def test_corner_case_large_numbers(self):
        self.assertEqual(Seq_Linear(list(range(1, 10001))), "Linear Sequence")
