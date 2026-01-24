import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):
    def test_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 4, 7, 11]), "Non Linear Sequence")

    def test_single_element_sequence(self):
        self.assertEqual(Seq_Linear([1]), "Linear Sequence")

    def test_empty_sequence(self):
        with self.assertRaises(IndexError):
            Seq_Linear([])

    def test_sequence_with_duplicates(self):
        self.assertEqual(Seq_Linear([1, 2, 2, 3, 3]), "Non Linear Sequence")

    def test_sequence_with_negative_numbers(self):
        self.assertEqual(Seq_Linear([-1, 0, 1]), "Linear Sequence")
