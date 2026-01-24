import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 4, 5, 7]), "Non Linear Sequence")

    def test_linear_sequence_with_negative_numbers(self):
        self.assertEqual(Seq_Linear([-1, 0, 1, 2, 3]), "Linear Sequence")

    def test_linear_sequence_with_zero(self):
        self.assertEqual(Seq_Linear([0, 0, 0, 0, 0]), "Linear Sequence")

    def test_non_linear_sequence_with_negative_numbers(self):
        self.assertEqual(Seq_Linear([-1, 2, 3, 4, 5]), "Non Linear Sequence")

    def test_non_linear_sequence_with_zero(self):
        self.assertEqual(Seq_Linear([0, 1, 2, 3, 4]), "Non Linear Sequence")

    def test_empty_sequence(self):
        with self.assertRaises(IndexError):
            Seq_Linear([])

    def test_sequence_with_one_element(self):
        with self.assertRaises(IndexError):
            Seq_Linear([1])
