import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_small_numbers(self):
        self.assertEqual(get_noOfways(2), 2)
        self.assertEqual(get_noOfways(3), 3)

    def test_larger_numbers(self):
        self.assertEqual(get_noOfways(4), 5)
        self.assertEqual(get_noOfways(5), 8)

    def test_negative_numbers(self):
        with self.assertRaisesRecursionLimit):
            get_noOfways(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            get_noOfways('a')
