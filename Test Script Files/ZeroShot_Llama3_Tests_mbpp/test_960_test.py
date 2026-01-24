import unittest
from mbpp_960_code import get_noOfways

class TestGetNoOfways(unittest.TestCase):

    def test_get_noOfways_zero(self):
        self.assertEqual(get_noOfways(0), 0)

    def test_get_noOfways_one(self):
        self.assertEqual(get_noOfways(1), 1)

    def test_get_noOfways_two(self):
        self.assertEqual(get_noOfways(2), 2)

    def test_get_noOfways_three(self):
        self.assertEqual(get_noOfways(3), 2)

    def test_get_noOfways_four(self):
        self.assertEqual(get_noOfways(4), 3)

    def test_get_noOfways_five(self):
        self.assertEqual(get_noOfways(5), 5)

    def test_get_noOfways_six(self):
        self.assertEqual(get_noOfways(6), 8)

    def test_get_noOfways_seven(self):
        self.assertEqual(get_noOfways(7), 13)

    def test_get_noOfways_eight(self):
        self.assertEqual(get_noOfways(8), 21)

    def test_get_noOfways_nine(self):
        self.assertEqual(get_noOfways(9), 34)

    def test_get_noOfways_ten(self):
        self.assertEqual(get_noOfways(10), 55)
