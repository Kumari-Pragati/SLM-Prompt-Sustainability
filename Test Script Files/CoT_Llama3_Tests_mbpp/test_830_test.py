import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):
    def test_round_up_positive(self):
        self.assertEqual(round_up(1.5, 0), 2)
        self.assertEqual(round_up(1.5, 1), 2.0)
        self.assertEqual(round_up(1.5, 2), 2.00)
        self.assertEqual(round_up(1.5, 3), 2.000)

    def test_round_up_negative(self):
        self.assertEqual(round_up(-1.5, 0), -2)
        self.assertEqual(round_up(-1.5, 1), -2.0)
        self.assertEqual(round_up(-1.5, 2), -2.00)
        self.assertEqual(round_up(-1.5, 3), -2.000)

    def test_round_up_zero(self):
        self.assertEqual(round_up(0, 0), 0)
        self.assertEqual(round_up(0, 1), 0.0)
        self.assertEqual(round_up(0, 2), 0.00)
        self.assertEqual(round_up(0, 3), 0.000)

    def test_round_up_edge_cases(self):
        self.assertEqual(round_up(1.0, 0), 1)
        self.assertEqual(round_up(1.0, 1), 1.0)
        self.assertEqual(round_up(1.0, 2), 1.00)
        self.assertEqual(round_up(1.0, 3), 1.000)

    def test_round_up_invalid_input(self):
        with self.assertRaises(TypeError):
            round_up('a', 1)
        with self.assertRaises(TypeError):
            round_up(1, 'a')
