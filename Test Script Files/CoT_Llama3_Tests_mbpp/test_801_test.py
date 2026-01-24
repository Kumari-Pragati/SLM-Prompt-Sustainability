import unittest
from mbpp_801_code import test_three_equal

class TestTestThreeEqual(unittest.TestCase):
    def test_three_equal_true(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_three_equal_false(self):
        self.assertEqual(test_three_equal(1, 1, 1), 2)

    def test_three_equal_single(self):
        self.assertEqual(test_three_equal(1, 1, 1), 1)

    def test_three_equal_empty(self):
        with self.assertRaises(TypeError):
            test_three_equal()

    def test_three_equal_non_integer(self):
        with self.assertRaises(TypeError):
            test_three_equal('a', 'b', 'c')
