import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):

    def test_minimum_equal(self):
        self.assertEqual(minimum(5, 5), 5)

    def test_minimum_a_smaller(self):
        self.assertEqual(minimum(3, 7), 3)

    def test_minimum_b_smaller(self):
        self.assertEqual(minimum(7, 3), 3)

    def test_minimum_a_greater(self):
        self.assertEqual(minimum(10, 5), 5)

    def test_minimum_b_greater(self):
        self.assertEqual(minimum(5, 10), 5)
