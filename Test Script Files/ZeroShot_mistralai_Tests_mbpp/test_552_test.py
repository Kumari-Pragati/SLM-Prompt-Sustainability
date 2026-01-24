import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Seq_Linear([]), "Non Linear Sequence")

    def test_single_element(self):
        self.assertEqual(Seq_Linear([1]), "Non Linear Sequence")

    def test_constant_sequence(self):
        self.assertEqual(Seq_Linear([1, 1, 1]), "Linear Sequence")

    def test_increasing_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")

    def test_decreasing_sequence(self):
        self.assertEqual(Seq_Linear([5, 4, 3, 2, 1]), "Linear Sequence")

    def test_mixed_sequence(self):
        self.assertEqual(Seq_Linear([1, 3, 2, 4, 5]), "Non Linear Sequence")

    def test_sequence_with_zero(self):
        self.assertEqual(Seq_Linear([0, 1, 2, 3, 4]), "Non Linear Sequence")
