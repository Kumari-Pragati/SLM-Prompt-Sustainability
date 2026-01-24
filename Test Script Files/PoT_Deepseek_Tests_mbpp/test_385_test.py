import unittest
from mbpp_385_code import get_perrin

class TestGetPerrin(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_perrin(0), 3)
        self.assertEqual(get_perrin(1), 0)
        self.assertEqual(get_perrin(2), 2)
        self.assertEqual(get_perrin(3), 2)
        self.assertEqual(get_perrin(4), 4)
        self.assertEqual(get_perrin(5), 5)
        self.assertEqual(get_perrin(6), 9)
        self.assertEqual(get_perrin(7), 12)

    def test_edge_cases(self):
        self.assertEqual(get_perrin(-1), 3)
        self.assertEqual(get_perrin(-10), 3)
        self.assertEqual(get_perrin(-100), 3)

    def test_boundary_cases(self):
        self.assertEqual(get_perrin(8), 20)
        self.assertEqual(get_perrin(9), 33)
        self.assertEqual(get_perrin(10), 52)

    def test_corner_cases(self):
        self.assertEqual(get_perrin(100), 19448)
        self.assertEqual(get_perrin(200), 2865788146)
