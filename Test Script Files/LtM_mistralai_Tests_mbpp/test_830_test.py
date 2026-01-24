import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(round_up(10.5, 1), 11.0)
        self.assertEqual(round_up(100.5, 2), 100.0)
        self.assertEqual(round_up(1000.5, 3), 1000.0)

    def test_edge_and_boundary(self):
        self.assertEqual(round_up(0.0, 1), 0.0)
        self.assertEqual(round_up(0.1, 1), 0.1)
        self.assertEqual(round_up(9.9, 1), 10.0)
        self.assertEqual(round_up(10.0, 0), 10)
        self.assertEqual(round_up(10.0, -1), 100.0)

    def test_complex(self):
        self.assertEqual(round_up(-10.5, 1), -11.0)
        self.assertEqual(round_up(0.0000001, 7), 0.0000001)
        self.assertEqual(round_up(math.pi, 2), round(math.ceil(math.pi * 100) / 100, 2))
