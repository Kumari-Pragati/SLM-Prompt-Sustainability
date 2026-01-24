import unittest
from mbpp_801_code import test_three_equal

class TestTestThreeEqual(unittest.TestCase):
    def test_three_unique_numbers(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_three_equal_numbers(self):
        self.assertEqual(test_three_equal(1, 1, 1), 0)

    def test_two_equal_numbers(self):
        self.assertEqual(test_three_equal(1, 1, 2), 2)

    def test_one_equal_numbers(self):
        self.assertEqual(test_three_equal(1, 2, 2), 2)

    def test_no_equal_numbers(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            test_three_equal()
