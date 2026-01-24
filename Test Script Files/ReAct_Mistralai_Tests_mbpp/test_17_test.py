import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_square_perimeter_positive(self):
        """Test square perimeter for positive integer inputs"""
        for side_length in [1, 2, 5, 10]:
            with self.subTest(f"side_length={side_length}"):
                result = square_perimeter(side_length)
                self.assertEqual(result, 4 * side_length)

    def test_square_perimeter_zero(self):
        """Test square perimeter for zero input"""
        with self.subTest("zero input"):
            result = square_perimeter(0)
            self.assertEqual(result, 0)

    def test_square_perimeter_negative(self):
        """Test square perimeter for negative integer inputs"""
        for side_length in [-1, -5, -10]:
            with self.subTest(f"side_length={side_length}"):
                result = square_perimeter(side_length)
                self.assertEqual(result, 4 * side_length)
