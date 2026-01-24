import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_find_divides_evenly(self):
        self.assertEqual(find(24, 4), 6)
        self.assertEqual(find(60, 15), 4)
        self.assertEqual(find(100, 25), 4)

    def test_find_divides_exactly(self):
        self.assertEqual(find(18, 2), 9)
        self.assertEqual(find(20, 4), 5)
        self.assertEqual(find(25, 5), 5)

    def test_find_divides_with_remainder(self):
        self.assertEqual(find(17, 2), 8)
        self.assertEqual(find(23, 3), 7)
        self.assertEqual(find(31, 4), 7)
