import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):

    def test_three_equal_same_numbers(self):
        """Test if three equal numbers return 0"""
        self.assertEqual(test_three_equal(1, 1, 1), 0)
        self.assertEqual(test_three_equal(2, 2, 2), 0)
        self.assertEqual(test_three_equal(3, 3, 3), 0)

    def test_three_equal_different_numbers(self):
        """Test if three different numbers return the correct error value"""
        self.assertEqual(test_three_equal(1, 2, 3), 1)
        self.assertEqual(test_three_equal(2, 3, 4), 1)
        self.assertEqual(test_three_equal(3, 4, 5), 1)

    def test_two_equal_and_one_different(self):
        """Test if two equal and one different number return the correct error value"""
        self.assertEqual(test_three_equal(1, 1, 2), 2)
        self.assertEqual(test_three_equal(2, 2, 3), 2)
        self.assertEqual(test_three_equal(3, 3, 4), 2)

    def test_one_equal_and_two_different(self):
        """Test if one equal and two different numbers return the correct error value"""
        self.assertEqual(test_three_equal(1, 2, 3), 2)
        self.assertEqual(test_three_equal(2, 1, 3), 2)
        self.assertEqual(test_three_equal(3, 2, 1), 2)

    def test_empty_set(self):
        """Test if an empty set raises a ValueError"""
        with self.assertRaises(ValueError):
            test_three_equal(1, 2, 3)

    def test_one_element_set(self):
        """Test if a set with one element raises a ValueError"""
        with self.assertRaises(ValueError):
            test_three_equal(1, 1, set())
