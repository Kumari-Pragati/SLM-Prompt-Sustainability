import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_simple_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")

    def test_simple_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 3, 5, 7, 9]), "Non Linear Sequence")

    def test_empty_sequence(self):
        self.assertEqual(Seq_Linear([]), "Non Linear Sequence")

    def test_single_element_sequence(self):
        self.assertEqual(Seq_Linear([5]), "Non Linear Sequence")

    def test_negative_numbers_sequence(self):
        self.assertEqual(Seq_Linear([-1, 0, 1, 2, 3]), "Non Linear Sequence")

    def test_large_numbers_sequence(self):
        self.assertEqual(Seq_Linear([1000, 2000, 3000, 4000, 5000]), "Linear Sequence")

    def test_sequence_with_zero(self):
        self.assertEqual(Seq_Linear([0, 1, 2, 3, 4]), "Non Linear Sequence")

    def test_sequence_with_same_difference(self):
        self.assertEqual(Seq_Linear([1, 4, 7, 10, 13]), "Linear Sequence")

    def test_sequence_with_different_difference(self):
        self.assertEqual(Seq_Linear([1, 3, 6, 10, 15]), "Non Linear Sequence")
