import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_smallest_multiple_1(self):
        self.assertEqual(smallest_multiple(1), 2)

    def test_smallest_multiple_2(self):
        self.assertEqual(smallest_multiple(2), 2)

    def test_smallest_multiple_3(self):
        self.assertEqual(smallest_multiple(3), 6)

    def test_smallest_multiple_4(self):
        self.assertEqual(smallest_multiple(4), 4)

    def test_smallest_multiple_5(self):
        self.assertEqual(smallest_multiple(5), 10)

    def test_smallest_multiple_6(self):
        self.assertEqual(smallest_multiple(6), 6)

    def test_smallest_multiple_7(self):
        self.assertEqual(smallest_multiple(7), 14)

    def test_smallest_multiple_8(self):
        self.assertEqual(smallest_multiple(8), 8)

    def test_smallest_multiple_9(self):
        self.assertEqual(smallest_multiple(9), 18)

    def test_smallest_multiple_10(self):
        self.assertEqual(smallest_multiple(10), 20)

    def test_smallest_multiple_11(self):
        self.assertEqual(smallest_multiple(11), 22)

    def test_smallest_multiple_12(self):
        self.assertEqual(smallest_multiple(12), 12)

    def test_smallest_multiple_13(self):
        self.assertEqual(smallest_multiple(13), 26)

    def test_smallest_multiple_14(self):
        self.assertEqual(smallest_multiple(14), 14)

    def test_smallest_multiple_15(self):
        self.assertEqual(smallest_multiple(15), 30)
