import unittest
from mbpp_385_code import get_perrin

class TestGetPerrin(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_perrin(0), 3)
        self.assertEqual(get_perrin(1), 0)
        self.assertEqual(get_perrin(2), 2)
        self.assertEqual(get_perrin(3), get_perrin(1) + get_perrin(0))
        self.assertEqual(get_perrin(4), get_perrin(2) + get_perrin(1))
        self.assertEqual(get_perrin(5), get_perrin(3) + get_perrin(2))
        self.assertEqual(get_perrin(6), get_perrin(4) + get_perrin(2))
        self.assertEqual(get_perrin(7), get_perrin(5) + get_perrin(3))
        self.assertEqual(get_perrin(8), get_perrin(6) + get_perrin(4))
        self.assertEqual(get_perrin(9), get_perrin(7) + get_perrin(5))

    def test_edge_cases(self):
        self.assertEqual(get_perrin(-1), None)
        self.assertEqual(get_perrin(0), 3)
        self.assertEqual(get_perrin(1), 0)
        self.assertEqual(get_perrin(2), 2)
        self.assertEqual(get_perrin(30), get_perrin(28) + get_perrin(26))
        self.assertEqual(get_perrin(100), get_perrin(98) + get_perrin(96))
