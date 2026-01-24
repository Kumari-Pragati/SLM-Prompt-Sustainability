import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):
    def test_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 4, 5, 7]), "Non Linear Sequence")

    def test_empty_input(self):
        with self.assertRaises(IndexError):
            Seq_Linear([])

    def test_single_element_input(self):
        self.assertEqual(Seq_Linear([1]), "Non Linear Sequence")

    def test_all_equal_input(self):
        self.assertEqual(Seq_Linear([1, 1, 1, 1, 1]), "Linear Sequence")

    def test_all_equal_input_with_zero(self):
        self.assertEqual(Seq_Linear([0, 0, 0, 0, 0]), "Linear Sequence")

    def test_all_equal_input_with_negative(self):
        self.assertEqual(Seq_Linear([-1, -1, -1, -1, -1]), "Linear Sequence")

    def test_all_equal_input_with_negative_and_positive(self):
        self.assertEqual(Seq_Linear([-1, 0, 1, 2, 3]), "Linear Sequence")
