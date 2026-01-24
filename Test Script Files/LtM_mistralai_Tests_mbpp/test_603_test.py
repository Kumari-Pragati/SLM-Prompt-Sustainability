import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(get_ludic(3), [1, 2, 3])
        self.assertEqual(get_ludic(5), [1, 3, 5])
        self.assertEqual(get_ludic(7), [1, 4, 7])

    def test_edge_cases(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(2), [1, 2])
        self.assertEqual(get_ludic(4), [1, 3])

    def test_boundary_conditions(self):
        self.assertEqual(get_ludic(0), [])
        self.assertEqual(get_ludic(-1), [])

    def test_complex_cases(self):
        self.assertEqual(get_ludic(10), [1, 3, 7, 10])
        self.assertEqual(get_ludic(15), [1, 4, 7, 13, 15])
        self.assertEqual(get_ludic(20), [1, 5, 11, 19, 20])
