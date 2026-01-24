import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):
    def test_linear_sequence(self):
        seq_nums = [1, 2, 3, 4, 5]
        self.assertEqual(Seq_Linear(seq_nums), "Linear Sequence")

    def test_non_linear_sequence(self):
        seq_nums = [1, 2, 4, 7, 11]
        self.assertEqual(Seq_Linear(seq_nums), "Non Linear Sequence")

    def test_single_element_sequence(self):
        seq_nums = [1]
        self.assertEqual(Seq_Linear(seq_nums), "Linear Sequence")

    def test_empty_sequence(self):
        seq_nums = []
        with self.assertRaises(IndexError):
            Seq_Linear(seq_nums)

    def test_sequence_with_negative_numbers(self):
        seq_nums = [-1, -2, -3, -4, -5]
        self.assertEqual(Seq_Linear(seq_nums), "Linear Sequence")

    def test_sequence_with_floating_point_numbers(self):
        seq_nums = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(Seq_Linear(seq_nums), "Linear Sequence")
