import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(Find_Min_Length([1, 2, 3]), 1)
        self.assertEqual(Find_Min_Length(["hello", "world"]), 5)
        self.assertEqual(Find_Min_Length([1, 2, 3, 4]), 1)

    def test_edge_cases(self):
        self.assertEqual(Find_Min_Length([]), 0)
        self.assertEqual(Find_Min_Length([1]), 1)
        self.assertEqual(Find_Min_Length([1, 0]), 1)
        self.assertEqual(Find_Min_Length([1, 2, 0]), 2)
        self.assertEqual(Find_Min_Length([0, 0]), 0)

    def test_complex_cases(self):
        self.assertEqual(Find_Min_Length([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(Find_Min_Length([10, 20, 30, 40, 50, 60]), 2)
        self.assertEqual(Find_Min_Length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(Find_Min_Length([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), 2)
        self.assertEqual(Find_Min_Length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 1)
