import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_parabola_directrix(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -11)
        self.assertEqual(parabola_directrix(2, 3, 4), -15)
        self.assertEqual(parabola_directrix(3, 4, 5), -19)
        self.assertEqual(parabola_directrix(4, 5, 6), -23)
        self.assertEqual(parabola_directrix(5, 6, 7), -27)

    def test_parabola_directrix_invalid_input(self):
        with self.assertRaises(TypeError):
            parabola_directrix('a', 2, 3)
        with self.assertRaises(TypeError):
            parabola_directrix(1, 'b', 3)
        with self.assertRaises(TypeError):
            parabola_directrix(1, 2, 'c')
