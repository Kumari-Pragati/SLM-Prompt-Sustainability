import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):
    def test_get_ludic_typical(self):
        self.assertEqual(get_ludic(5), [1, 2, 3, 4, 5])

    def test_get_ludic_edge(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(2), [1, 2])

    def test_get_ludic_boundary(self):
        self.assertEqual(get_ludic(10), list(range(1, 11)))

    def test_get_ludic_invalid_input(self):
        with self.assertRaises(TypeError):
            get_ludic('a')

    def test_get_ludic_negative_input(self):
        with self.assertRaises(TypeError):
            get_ludic(-1)
