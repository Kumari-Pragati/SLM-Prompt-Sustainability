import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_small_positive(self):
        self.assertEqual(get_noOfways(2), 2)

    def test_small_positive(self):
        self.assertEqual(get_noOfways(3), 3)

    def test_large_positive(self):
        self.assertEqual(get_noOfways(5), 8)

    def test_negative(self):
        with self.assertRaisesRecursionLimitError:
            get_noOfways(-1)
