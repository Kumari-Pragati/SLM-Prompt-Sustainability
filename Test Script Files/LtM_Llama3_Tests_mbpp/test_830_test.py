import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(round_up(1.5, 0), 2)
        self.assertEqual(round_up(1.5, 1), 1.5)
        self.assertEqual(round_up(1.5, 2), 1.5)
        self.assertEqual(round_up(1.5, 3), 1.5)
        self.assertEqual(round_up(1.5, 4), 1.5)

    def test_edge(self):
        self.assertEqual(round_up(1.5, 5), 1.5)
        self.assertEqual(round_up(1.5, 6), 1.5)
        self.assertEqual(round_up(1.5, 7), 1.5)
        self.assertEqual(round_up(1.5, 8), 1.5)
        self.assertEqual(round_up(1.5, 9), 1.5)

    def test_edge2(self):
        self.assertEqual(round_up(1.5, -1), 2)
        self.assertEqual(round_up(1.5, -2), 2)
        self.assertEqual(round_up(1.5, -3), 2)
        self.assertEqual(round_up(1.5, -4), 2)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            round_up('a', 0)
        with self.assertRaises(TypeError):
            round_up(1.5, 'a')
