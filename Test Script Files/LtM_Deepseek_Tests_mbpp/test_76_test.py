import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Squares(2, 3), 5)
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(5, 5), 16)

    def test_edge_conditions(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(100, 100), 338350)
        self.assertEqual(count_Squares(0, 10), 0)
        self.assertEqual(count_Squares(10, 0), 0)

    def test_complex_cases(self):
        self.assertEqual(count_Squares(15, 20), 1365)
        self.assertEqual(count_Squares(20, 15), 1365)
        self.assertEqual(count_Squares(100, 200), 496050)
