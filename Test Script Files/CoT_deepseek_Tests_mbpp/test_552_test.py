import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")
        self.assertEqual(Seq_Linear([10, 20, 30, 40, 50]), "Linear Sequence")
        self.assertEqual(Seq_Linear([0, 10, 20, 30, 40]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 3, 9, 27, 81]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([1, 2, 4, 8, 16]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([1, 2, 3, 5, 8]), "Non Linear Sequence")

    def test_single_element(self):
        self.assertEqual(Seq_Linear([1]), "Non Linear Sequence")

    def test_empty_sequence(self):
        self.assertEqual(Seq_Linear([]), "Non Linear Sequence")

    def test_negative_numbers(self):
        self.assertEqual(Seq_Linear([-1, 0, 1, 2, 3]), "Non Linear Sequence")

    def test_zero_difference(self):
        self.assertEqual(Seq_Linear([0, 0, 0, 0, 0]), "Non Linear Sequence")
