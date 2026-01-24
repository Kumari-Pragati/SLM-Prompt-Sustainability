import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Squares(2, 3), 6)
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(5, 5), 35)

    def test_edge_conditions(self):
        self.assertEqual(count_Squares(0, 1), 0)
        self.assertEqual(count_Squares(1, 0), 0)
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(1000, 1000), 500500)

    def test_complex_cases(self):
        self.assertEqual(count_Squares(10, 20), 210)
        self.assertEqual(count_Squares(20, 10), 210)
        self.assertEqual(count_Squares(15, 25), 455)
