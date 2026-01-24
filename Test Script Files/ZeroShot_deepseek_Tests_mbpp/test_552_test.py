import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")
        self.assertEqual(Seq_Linear([10, 20, 30, 40, 50]), "Linear Sequence")
        self.assertEqual(Seq_Linear([100, 200, 300, 400, 500]), "Linear Sequence")

    def test_non_linear_sequence(self):
        self.assertEqual(Seq_Linear([1, 2, 4, 7, 11]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([10, 22, 34, 46, 58]), "Non Linear Sequence")
        self.assertEqual(Seq_Linear([100, 201, 302, 403, 504]), "Non Linear Sequence")
