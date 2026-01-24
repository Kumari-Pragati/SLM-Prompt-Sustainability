import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(9), 16)

    def test_edge_conditions(self):
        self.assertEqual(next_Perfect_Square(0), 1)
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(8), 9)
        self.assertEqual(next_Perfect_Square(9), 16)
        self.assertEqual(next_Perfect_Square(15), 16)
        self.assertEqual(next_Perfect_Square(16), 25)

    def test_complex_cases(self):
        self.assertEqual(next_Perfect_Square(144), 169)
        self.assertEqual(next_Perfect_Square(244), 289)
        self.assertEqual(next_Perfect_Square(361), 400)
