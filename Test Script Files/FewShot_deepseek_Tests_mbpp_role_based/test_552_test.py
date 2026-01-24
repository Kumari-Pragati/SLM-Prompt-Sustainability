import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")

    def test_edge_condition(self):
        self.assertEqual(Seq_Linear([1]), "Linear Sequence")

    def test_boundary_condition(self):
        self.assertEqual(Seq_Linear([1, 2]), "Linear Sequence")
        self.assertEqual(Seq_Linear([1, 2, 3]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 3, 5, 7, 9]), "Non Linear Sequence")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Seq_Linear("1, 2, 3, 4, 5")

        with self.assertRaises(TypeError):
            Seq_Linear(12345)

        with self.assertRaises(TypeError):
            Seq_Linear(None)
