import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):
    def test_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")
        self.assertEqual(Seq_Linear([0, 1, 2, 3, 4]), "Linear Sequence")
        self.assertEqual(Seq_Linear([-1, -2, -3, -4, -5]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5, 6]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([0, 2, 4, 6, 8]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([-1, -2, -3, -4, -6]), "Non Linear Sequence")

    def test_single_element(self):
        self.assertEqual(Seq_Linear([1]), "Linear Sequence")
        self.assertEqual(Seq_Linear([0]), "Linear Sequence")
        self.assertEqual(Seq_Linear([-1]), "Linear Sequence")

    def test_empty_list(self):
        self.assertEqual(Seq_Linear([]), "Non Linear Sequence")

    def test_negative_differences(self):
        self.assertEqual(Seq_Linear([-1, 0, -1]), "Linear Sequence")
        self.assertEqual(Seq_Linear([-2, -1, 0]), "Non Linear Sequence")
