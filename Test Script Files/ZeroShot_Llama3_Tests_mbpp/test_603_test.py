import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_get_ludic(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(2), [1, 2])
        self.assertEqual(get_ludic(3), [1, 2, 3])
        self.assertEqual(get_ludic(4), [1, 2, 3, 4])
        self.assertEqual(get_ludic(5), [1, 1, 2, 3, 4, 5])
        self.assertEqual(get_ludic(6), [1, 1, 2, 3, 4, 5, 6])
        self.assertEqual(get_ludic(7), [1, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(get_ludic(8), [1, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(get_ludic(9), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(get_ludic(10), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_get_ludic_edge_cases(self):
        self.assertEqual(get_ludic(0), [])
