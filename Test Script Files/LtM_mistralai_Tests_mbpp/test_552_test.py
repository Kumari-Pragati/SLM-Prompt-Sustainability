import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_simple_linear(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4]), "Linear Sequence")

    def test_simple_non_linear(self):
        self.assertEqual(Seq_Linear([2, 4, 6, 8]), "Non Linear Sequence")

    def test_edge_single_element(self):
        self.assertEqual(Seq_Linear([1]), "Linear Sequence")

    def test_edge_two_elements(self):
        self.assertEqual(Seq_Linear([1, 2]), "Linear Sequence")

    def test_edge_increasing_then_decreasing(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 2]), "Non Linear Sequence")

    def test_edge_decreasing_then_increasing(self):
        self.assertEqual(Seq_Linear([2, 1, 2, 3]), "Non Linear Sequence")

    def test_edge_constant_sequence(self):
        self.assertEqual(Seq_Linear([1, 1, 1, 1]), "Linear Sequence")

    def test_edge_negative_sequence(self):
        self.assertEqual(Seq_Linear([-1, -2, -3]), "Linear Sequence")

    def test_edge_zero_sequence(self):
        self.assertEqual(Seq_Linear([0, 0, 0]), "Linear Sequence")

    def test_complex_alternating_sequence(self):
        self.assertEqual(Seq_Linear([1, -1, 1, -1, 1]), "Non Linear Sequence")
