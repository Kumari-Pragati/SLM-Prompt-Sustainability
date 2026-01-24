import unittest
from mbpp_385_code import get_perrin

class TestGetPerrin(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(get_perrin(0), 3)
        self.assertEqual(get_perrin(1), 0)
        self.assertEqual(get_perrin(2), 2)
        self.assertEqual(get_perrin(3), 5)
        self.assertEqual(get_perrin(4), 7)
        self.assertEqual(get_perrin(5), 12)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(get_perrin(-1), None)
        self.assertEqual(get_perrin(6), None)
        self.assertEqual(get_perrin(0.5), None)
        self.assertEqual(get_perrin('str'), None)
