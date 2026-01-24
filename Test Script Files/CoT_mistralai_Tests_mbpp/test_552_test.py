import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):
    def test_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")
        self.assertEqual(Seq_Linear([0, 1, 2, 3, 4]), "Linear Sequence")
        self.assertEqual(Seq_Linear([-1, -2, -3, -4, -5]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 5, 7]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([0, 1, 2, 4, 6]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([-1, -2, -4, -5, -7]), "Non Linear Sequence")

    def test_single_element(self):
        self.assertEqual(Seq_Linear([1]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([0]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([-1]), "Non Linear Sequence")

    def test_empty_list(self):
        self.assertRaises(ValueError, Seq_Linear, [])

    def test_negative_index(self):
        self.assertRaises(IndexError, Seq_Linear, [-1, 0, 1])
