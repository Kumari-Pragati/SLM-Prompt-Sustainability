import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_smallest_multiple_1(self):
        self.assertEqual(smallest_multiple(1), 1)

    def test_smallest_multiple_2(self):
        self.assertEqual(smallest_multiple(2), 2)

    def test_smallest_multiple_3(self):
        self.assertEqual(smallest_multiple(3), 6)

    def test_smallest_multiple_4(self):
        self.assertEqual(smallest_multiple(4), 12)

    def test_smallest_multiple_5(self):
        self.assertEqual(smallest_multiple(5), 60)

    def test_smallest_multiple_6(self):
        self.assertEqual(smallest_multiple(6), 60)

    def test_smallest_multiple_7(self):
        self.assertEqual(smallest_multiple(7), 420)

    def test_smallest_multiple_8(self):
        self.assertEqual(smallest_multiple(8), 840)

    def test_smallest_multiple_9(self):
        self.assertEqual(smallest_multiple(9), 2520)

    def test_smallest_multiple_10(self):
        self.assertEqual(smallest_multiple(10), 2520)
