import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_typical_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")

    def test_typical_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 3, 5, 7, 9]), "Non Linear Sequence")

    def test_single_element_sequence(self):
        self.assertEqual(Seq_Linear([5]), "Linear Sequence")

    def test_empty_sequence(self):
        self.assertEqual(Seq_Linear([]), "Non Linear Sequence")

    def test_negative_numbers_sequence(self):
        self.assertEqual(Seq_Linear([-1, 0, 1, 2, 3]), "Linear Sequence")

    def test_zero_difference_sequence(self):
        self.assertEqual(Seq_Linear([0, 0, 0, 0]), "Non Linear Sequence")

    def test_large_numbers_sequence(self):
        self.assertEqual(Seq_Linear([100, 200, 300, 400]), "Linear Sequence")

    def test_float_numbers_sequence(self):
        self.assertEqual(Seq_Linear([1.0, 2.0, 3.0, 4.0]), "Linear Sequence")

    def test_mixed_numbers_sequence(self):
        self.assertEqual(Seq_Linear([1, 2.5, 4, 5.5]), "Non Linear Sequence")
