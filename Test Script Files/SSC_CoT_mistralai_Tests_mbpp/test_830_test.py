import unittest
from mbpp_830_code import round_up

class TestRoundUp(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(round_up(3.14, 2), 3.14)
        self.assertEqual(round_up(314.0, 2), 314.0)
        self.assertEqual(round_up(-3.14, 2), -3.14)
        self.assertEqual(round_up(-314.0, 2), -314.0)

    def test_edge_cases(self):
        self.assertEqual(round_up(3.0, 0), 3.0)
        self.assertEqual(round_up(3.5, 0), 4.0)
        self.assertEqual(round_up(3.0, -1), 10.0)
        self.assertEqual(round_up(3.5, -1), 40.0)
        self.assertEqual(round_up(0.0, 2), 0.0)
        self.assertEqual(round_up(0.5, 2), 1.0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, round_up, "not_a_number", 2)
        self.assertRaises(TypeError, round_up, 3, "not_an_integer")
        self.assertRaises(ValueError, round_up, -1, -1)
