import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_get_carol_with_zero(self):
        self.assertEqual(get_carol(0), 0)

    def test_get_carol_with_one(self):
        self.assertEqual(get_carol(1), 1)

    def test_get_carol_with_two(self):
        self.assertEqual(get_carol(2), 7)

    def test_get_carol_with_three(self):
        self.assertEqual(get_carol(3), 47)

    def test_get_carol_with_four(self):
        self.assertEqual(get_carol(4), 311)

    def test_get_carol_with_five(self):
        self.assertEqual(get_carol(5), 2047)
