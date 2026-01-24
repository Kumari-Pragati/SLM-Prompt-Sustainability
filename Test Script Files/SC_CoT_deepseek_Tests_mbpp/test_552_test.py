import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_typical_sequence(self):
        self.assertEqual(Seq_Linear([1, 3, 5, 7, 9]), "Linear Sequence")

    def test_edge_sequence(self):
        self.assertEqual(Seq_Linear([1]), "Linear Sequence")
        self.assertEqual(Seq_Linear([1, 2]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 3, 2, 4, 5]), "Non Linear Sequence")

    def test_empty_sequence(self):
        self.assertEqual(Seq_Linear([]), "Non Linear Sequence")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Seq_Linear("1, 2, 3, 4, 5")

        with self.assertRaises(TypeError):
            Seq_Linear(123)

        with self.assertRaises(TypeError):
            Seq_Linear(None)
