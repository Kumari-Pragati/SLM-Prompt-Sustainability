import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(next_Perfect_Square(16), 25)
        self.assertEqual(next_Perfect_Square(25), 49)
        self.assertEqual(next_Perfect_Square(49), 64)
        self.assertEqual(next_Perfect_Square(64), 81)

    def test_edge_cases(self):
        self.assertEqual(next_Perfect_Square(0), 1)
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(2), 9)
        self.assertEqual(next_Perfect_Square(3), 9)
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(5), 25)

    def test_boundary_cases(self):
        self.assertEqual(next_Perfect_Square(math.sqrt(float('inf'))), float('inf'))
        self.assertEqual(next_Perfect_Square(math.ceil(math.sqrt(float('-inf')))) * next_Perfect_Square(math.ceil(math.sqrt(float('-inf')))), float('-inf'))
