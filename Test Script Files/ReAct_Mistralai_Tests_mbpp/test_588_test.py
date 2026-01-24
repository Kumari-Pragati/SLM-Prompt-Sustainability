import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):

    def test_empty_list(self):
        """Test behavior with an empty list"""
        self.assertEqual(big_diff([]), 0)

    def test_single_element(self):
        """Test behavior with a single element list"""
        for num in [1, -1]:
            self.assertEqual(big_diff([num]), num)

    def test_positive_numbers(self):
        """Test behavior with a list of positive numbers"""
        self.assertEqual(big_diff([1, 2, 3, 4, 5]), 4)

    def test_negative_numbers(self):
        """Test behavior with a list of negative numbers"""
        self.assertEqual(big_diff([-1, -2, -3, -4, -5]), 5)

    def test_mixed_numbers(self):
        """Test behavior with a list of mixed numbers"""
        self.assertEqual(big_diff([1, -2, 3, -4, 5]), 7)

    def test_extreme_values(self):
        """Test behavior with extreme values"""
        self.assertEqual(big_diff([sys.maxsize, -sys.maxsize]), sys.maxsize * 2)
        self.assertEqual(big_diff([-sys.maxsize, sys.maxsize]), sys.maxsize * 2)

    def test_duplicate_values(self):
        """Test behavior with duplicate values"""
        self.assertEqual(big_diff([1, 1, 2, 3]), 2)

    def test_error_empty_input(self):
        """Test error handling for empty input"""
        with self.assertRaises(TypeError):
            big_diff()
