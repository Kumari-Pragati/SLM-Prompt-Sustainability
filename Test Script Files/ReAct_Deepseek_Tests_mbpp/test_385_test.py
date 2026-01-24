import unittest
from mbpp_385_code import get_perrin

class TestPerrin(unittest.TestCase):

    def test_get_perrin_typical_cases(self):
        self.assertEqual(get_perrin(0), 3)
        self.assertEqual(get_perrin(1), 0)
        self.assertEqual(get_perrin(2), 2)

    def test_get_perrin_edge_cases(self):
        self.assertEqual(get_perrin(3), 2)
        self.assertEqual(get_perrin(4), 2)
        self.assertEqual(get_perrin(5), 4)
        self.assertEqual(get_perrin(6), 5)
        self.assertEqual(get_perrin(7), 7)

    def test_get_perrin_negative_cases(self):
        with self.assertRaises(RecursionError):
            get_perrin(-1)

    def test_get_perrin_large_cases(self):
        self.assertEqual(get_perrin(20), 121415)
