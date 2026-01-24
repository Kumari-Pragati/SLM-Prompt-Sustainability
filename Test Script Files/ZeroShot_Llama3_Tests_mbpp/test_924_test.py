import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_max_of_two(self):
        self.assertEqual(max_of_two(1, 2), 2)
        self.assertEqual(max_of_two(10, 2), 10)
        self.assertEqual(max_of_two(5, 5), 5)
        self.assertEqual(max_of_two(-1, -2), -1)
        self.assertEqual(max_of_two(-10, -2), -2)
        self.assertEqual(max_of_two(0, 0), 0)
        self.assertEqual(max_of_two(-5, 5), 5)
        self.assertEqual(max_of_two(5, -5), 5)
        self.assertEqual(max_of_two(-5, 0), 0)
        self.assertEqual(max_of_two(0, -5), 0)
