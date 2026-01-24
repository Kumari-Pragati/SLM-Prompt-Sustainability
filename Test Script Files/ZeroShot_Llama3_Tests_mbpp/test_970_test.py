import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):
    def test_min_of_two(self):
        self.assertEqual(min_of_two(5, 3), 3)
        self.assertEqual(min_of_two(10, 20), 10)
        self.assertEqual(min_of_two(5, 5), 5)
        self.assertEqual(min_of_two(-5, -10), -10)
        self.assertEqual(min_of_two(0, 0), 0)
        self.assertEqual(min_of_two(-5, 0), -5)
        self.assertEqual(min_of_two(5, -5), -5)
