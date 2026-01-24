import unittest
from mbpp_522_code import lbs

class TestLbs(unittest.TestCase):

    def test_lbs(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5]), 5)
        self.assertEqual(lbs([5, 4, 3, 2, 1]), 5)
        self.assertEqual(lbs([1, 3, 2, 4, 5]), 5)
        self.assertEqual(lbs([5, 4, 3, 2, 1, 3, 4, 5, 2, 3, 1, 4]), 9)
        self.assertEqual(lbs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(lbs([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 10)
        self.assertEqual(lbs([1, 1, 1, 1, 1]), 1)
        self.assertEqual(lbs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 15)
        self.assertEqual(lbs([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 15)

    def test_lbs_empty(self):
        self.assertEqual(lbs([]), 0)

    def test_lbs_single(self):
        self.assertEqual(lbs([1]), 1)

    def test_lbs_two(self):
        self.assertEqual(lbs([1, 2]), 2)

    def test_lbs_three(self):
        self.assertEqual(lbs([1, 2, 3]), 3)

    def test_lbs_four(self):
        self.assertEqual(lbs([1, 2, 3, 4]), 4)

    def test_lbs_five(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5]), 5)
