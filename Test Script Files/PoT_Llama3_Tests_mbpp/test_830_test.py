import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(round_up(1.5, 0), 2)
        self.assertEqual(round_up(1.5, 1), 2.0)
        self.assertEqual(round_up(1.5, 2), 1.5)
        self.assertEqual(round_up(1.5, 3), 1.5)
        self.assertEqual(round_up(1.5, 4), 1.5000)
        self.assertEqual(round_up(1.5, 5), 1.50000)

    def test_edge(self):
        self.assertEqual(round_up(1.0, 0), 1)
        self.assertEqual(round_up(1.0, 1), 1.0)
        self.assertEqual(round_up(1.0, 2), 1.0)
        self.assertEqual(round_up(1.0, 3), 1.0)
        self.assertEqual(round_up(1.0, 4), 1.0000)
        self.assertEqual(round_up(1.0, 5), 1.00000)

    def test_boundary(self):
        self.assertEqual(round_up(1.0, 0), 1)
        self.assertEqual(round_up(1.0, 1), 1.0)
        self.assertEqual(round_up(1.0, 2), 1.0)
        self.assertEqual(round_up(1.0, 3), 1.0)
        self.assertEqual(round_up(1.0, 4), 1.0000)
        self.assertEqual(round_up(1.0, 5), 1.00000)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            round_up('a', 1)
        with self.assertRaises(TypeError):
            round_up(1, 'a')
