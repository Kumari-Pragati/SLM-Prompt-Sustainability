import unittest
from mbpp_552_code import Seq_Linear

class TestSeqLinear(unittest.TestCase):

    def test_empty_sequence(self):
        """Tests if an empty sequence returns 'Non Linear Sequence'"""
        self.assertEqual(Seq_Linear([]), "Non Linear Sequence")

    def test_single_element_sequence(self):
        """Tests if a sequence with one element returns 'Linear Sequence'"""
        self.assertEqual(Seq_Linear([1]), "Linear Sequence")

    def test_constant_sequence(self):
        """Tests if a constant sequence returns 'Non Linear Sequence'"""
        self.assertEqual(Seq_Linear([1, 1, 1]), "Non Linear Sequence")

    def test_increasing_sequence(self):
        """Tests if an increasing sequence returns 'Linear Sequence'"""
        self.assertEqual(Seq_Linear([1, 2, 3, 4, 5]), "Linear Sequence")

    def test_decreasing_sequence(self):
        """Tests if a decreasing sequence returns 'Linear Sequence'"""
        self.assertEqual(Seq_Linear([5, 4, 3, 2, 1]), "Linear Sequence")

    def test_alternating_sequence(self):
        """Tests if an alternating sequence returns 'Non Linear Sequence'"""
        self.assertEqual(Seq_Linear([1, 2, 1, 2, 1]), "Non Linear Sequence")

    def test_mixed_sequence(self):
        """Tests if a mixed sequence returns 'Non Linear Sequence'"""
        self.assertEqual(Seq_Linear([1, 2, 3, 2, 1]), "Non Linear Sequence")

    def test_duplicate_values(self):
        """Tests if a sequence with duplicate values returns 'Non Linear Sequence'"""
        self.assertEqual(Seq_Linear([1, 1, 2, 1]), "Non Linear Sequence")
