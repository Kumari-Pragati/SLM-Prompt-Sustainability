import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    def test_min_of_three_a_smallest(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)

    def test_min_of_three_b_smallest(self):
        self.assertEqual(min_of_three(3, 1, 2), 1)

    def test_min_of_three_c_smallest(self):
        self.assertEqual(min_of_three(2, 3, 1), 1)

    def test_min_of_three_a_and_b_equal(self):
        self.assertEqual(min_of_three(1, 1, 3), 1)

    def test_min_of_three_a_and_c_equal(self):
        self.assertEqual(min_of_three(1, 3, 1), 1)

    def test_min_of_three_b_and_c_equal(self):
        self.assertEqual(min_of_three(3, 1, 1), 1)

    def test_min_of_three_all_equal(self):
        self.assertEqual(min_of_three(1, 1, 1), 1)
