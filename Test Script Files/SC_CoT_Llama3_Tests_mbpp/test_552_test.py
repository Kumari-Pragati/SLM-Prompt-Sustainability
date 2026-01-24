import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 4, 7, 11]), "Non Linear Sequence")

    def test_linear_sequence_edge(self):
        self.assertEqual(Seq_Linear([1, 1, 1, 1, 1]), "Linear Sequence")

    def test_non_linear_sequence_edge(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5, 6]), "Non Linear Sequence")

    def test_linear_sequence_corner(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 3, 4, 5]), "Linear Sequence")

    def test_non_linear_sequence_corner(self):
        self.assertEqual(Seq_Linear([1, 2, 4, 7, 11, 15]), "Non Linear Sequence")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Seq_Linear("Invalid Input")
