import unittest
from mbpp_385_code import get_perrin

class TestGetPerrin(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(get_perrin(0), 3)
        self.assertEqual(get_perrin(1), 0)
        self.assertEqual(get_perrin(2), 2)

    def test_small_positive_numbers(self):
        self.assertEqual(get_perrin(3), 2)
        self.assertEqual(get_perrin(4), 5)
        self.assertEqual(get_perrin(5), 7)

    def test_large_positive_numbers(self):
        self.assertEqual(get_perrin(100), 247)
        self.assertEqual(get_perrin(200), 487)
        self.assertEqual(get_perrin(300), 737)

    def test_negative_numbers(self):
        self.assertEqual(get_perrin(-1), get_perrin(1))
        self.assertEqual(get_perrin(-2), get_perrin(2))
        self.assertEqual(get_perrin(-3), get_perrin(0))
