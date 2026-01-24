import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(9), 16)

    def test_edge_case(self):
        self.assertEqual(next_Perfect_Square(0), 1)
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(8), 9)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            next_Perfect_Square('a')
        with self.assertRaises(ValueError):
            next_Perfect_Square(-1)
