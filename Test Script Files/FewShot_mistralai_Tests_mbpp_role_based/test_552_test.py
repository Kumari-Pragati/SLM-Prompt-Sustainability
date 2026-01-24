import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):
    def test_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4]), "Linear Sequence")

    def test_constant_sequence(self):
        self.assertEqual(Seq_Linear([1, 1, 1, 1]), "Linear Sequence")

    def test_decreasing_sequence(self):
        self.assertEqual(Seq_Linear([5, 4, 3, 2]), "Non Linear Sequence")

    def test_increasing_then_decreasing_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 3, 2]), "Non Linear Sequence")

    def test_empty_sequence(self):
        self.assertRaises(IndexError, Seq_Linear, [])

    def test_single_element_sequence(self):
        self.assertEqual(Seq_Linear([1]), "Non Linear Sequence")
