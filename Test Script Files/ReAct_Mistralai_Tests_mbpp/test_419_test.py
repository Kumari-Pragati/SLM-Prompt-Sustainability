import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_empty_list(self):
        """Test round_and_sum with an empty list"""
        self.assertEqual(round_and_sum([]), 0)

    def test_single_element_list(self):
        """Test round_and_sum with a list containing one element"""
        self.assertEqual(round_and_sum([1.1]), 1)

    def test_positive_numbers(self):
        """Test round_and_sum with a list containing positive numbers"""
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 15)

    def test_negative_numbers(self):
        """Test round_and_sum with a list containing negative numbers"""
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3]), 15)

    def test_mixed_numbers(self):
        """Test round_and_sum with a list containing mixed numbers"""
        self.assertEqual(round_and_sum([1.1, -2.2, 3.3, -4.4]), 11)

    def test_zero(self):
        """Test round_and_sum with a list containing zero"""
        self.assertEqual(round_and_sum([0.0]), 0)

    def test_large_numbers(self):
        """Test round_and_sum with a list containing large numbers"""
        self.assertEqual(round_and_sum([1e10, 2e10, 3e10]), 6e11)

    def test_small_numbers(self):
        """Test round_and_sum with a list containing small numbers"""
        self.assertEqual(round_and_sum([1e-10, 2e-10, 3e-10]), 6e-10)

    def test_floats_and_integers(self):
        """Test round_and_sum with a list containing both floats and integers"""
        self.assertEqual(round_and_sum([1, 2.2, 3]), 12)

    def test_list_length(self):
        """Test round_and_sum with a list of different lengths"""
        self.assertEqual(round_and_sum([1.1]), 1)
        self.assertEqual(round_and_sum([1.1, 2.2]), 4)
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3, 4.4, 5.5]), 35)
