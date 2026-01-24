import unittest
from mbpp_177_code import answer

class TestAnswerFunction(unittest.TestCase):

    def test_positive_input(self):
        """Test correct output for positive inputs"""
        self.assertEqual(answer(1, 4), (1, 2))
        self.assertEqual(answer(2, 8), (2, 4))
        self.assertEqual(answer(3, 12), (3, 6))

    def test_zero_input(self):
        """Test correct output for zero input"""
        self.assertEqual(answer(0, 2), (-1))

    def test_negative_input(self):
        """Test correct output for negative inputs"""
        self.assertEqual(answer(-1, 0), (-1))
        self.assertEqual(answer(-2, -4), (-1))
        self.assertEqual(answer(-3, -6), (-1))

    def test_boundary_cases(self):
        """Test correct output for boundary cases"""
        self.assertEqual(answer(1, 2), (-1))
        self.assertEqual(answer(2, 3), (-1))
