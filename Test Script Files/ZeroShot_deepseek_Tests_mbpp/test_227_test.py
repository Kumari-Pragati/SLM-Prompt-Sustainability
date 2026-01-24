import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    def test_min_of_three(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(3, 2, 1), 1)
        self.assertEqual(min_of_three(2, 1, 3), 1)
        self.assertEqual(min_of_three(1, 1, 1), 1)
        self.assertEqual(min_of_three(0, -1, -2), -2)
        self.assertEqual(min_of_three(-1, -2, -3), -3)
        self.assertEqual(min_of_three(-1, 0, 1), -1)
