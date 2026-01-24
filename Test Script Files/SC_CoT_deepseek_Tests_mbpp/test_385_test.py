import unittest
from mbpp_385_code import get_perrin

class TestPerrin(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_perrin(0), 3)
        self.assertEqual(get_perrin(1), 0)
        self.assertEqual(get_perrin(2), 2)

    def test_edge_cases(self):
        self.assertEqual(get_perrin(3), 2)
        self.assertEqual(get_perrin(4), 4)
        self.assertEqual(get_perrin(5), 5)
        self.assertEqual(get_perrin(6), 9)
        self.assertEqual(get_perrin(7), 12)

    def test_corner_cases(self):
        self.assertEqual(get_perrin(10), 447)
        self.assertEqual(get_perrin(20), 52265)
        self.assertEqual(get_perrin(30), 1056050)

    def test_invalid_inputs(self):
        with self.assertRaises(RecursionError):
            get_perrin(-1)
        with self.assertRaises(TypeError):
            get_perrin('a')
