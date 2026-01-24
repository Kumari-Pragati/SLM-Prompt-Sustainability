import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfWays(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_two(self):
        self.assertEqual(get_noOfways(2), 2)

    def test_three(self):
        self.assertEqual(get_noOfways(3), 2)

    def test_negative(self):
        with self.assertRaisesRecursives(RecursionError):
            get_noOfways(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            get_noOfways('a')
