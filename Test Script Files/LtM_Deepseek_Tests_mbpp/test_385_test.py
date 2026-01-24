import unittest
from mbpp_385_code import get_perrin

class TestPerrin(unittest.TestCase):
    def test_get_perrin_simple(self):
        self.assertEqual(get_perrin(0), 3)
        self.assertEqual(get_perrin(1), 0)
        self.assertEqual(get_perrin(2), 2)

    def test_get_perrin_edge(self):
        self.assertEqual(get_perrin(-1), 0)
        self.assertEqual(get_perrin(-2), 3)
        self.assertEqual(get_perrin(-3), 0)

    def test_get_perrin_complex(self):
        self.assertEqual(get_perrin(3), 2)
        self.assertEqual(get_perrin(4), 4)
        self.assertEqual(get_perrin(5), 5)
        self.assertEqual(get_perrin(6), 7)
        self.assertEqual(get_perrin(7), 10)
