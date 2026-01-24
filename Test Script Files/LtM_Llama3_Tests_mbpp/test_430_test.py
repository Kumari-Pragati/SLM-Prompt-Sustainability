import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(parabola_directrix(1, 2, 3), -5)
        self.assertEqual(parabola_directrix(2, 3, 4), -3)
        self.assertEqual(parabola_directrix(3, 4, 5), -1)

    def test_edge_cases(self):
        self.assertEqual(parabola_directrix(1, 0, 0), 0)
        self.assertEqual(parabola_directrix(1, 1, 1), 0)
        self.assertEqual(parabola_directrix(1, 2, 3), -5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parabola_directrix('a', 2, 3)
        with self.assertRaises(TypeError):
            parabola_directrix(1, 'b', 3)
        with self.assertRaises(TypeError):
            parabola_directrix(1, 2, 'c')
