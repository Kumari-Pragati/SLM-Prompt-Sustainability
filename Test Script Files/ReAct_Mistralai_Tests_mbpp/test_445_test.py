import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_empty_tuples(self):
        """Test empty tuples"""
        self.assertEqual(index_multiplication((), ()), ())

    def test_single_element_tuples(self):
        """Test single element tuples"""
        self.assertEqual(index_multiplication((1), (2)), ((1 * 2,)))
        self.assertEqual(index_multiplication(((1)), ((2,))) , (((1 * 2,)),))

    def test_tuples_with_different_lengths(self):
        """Test tuples with different lengths"""
        self.assertRaises(ValueError, index_multiplication, ((1, 2), (3)), ((4, 5, 6)))

    def test_positive_integer_tuples(self):
        """Test positive integer tuples"""
        self.assertEqual(index_multiplication((1, 2), (3, 4)), ((3 * 1, 4 * 2),))
        self.assertEqual(index_multiplication(((1, 2)), ((3, 4, 5))) , (((3 * 1, 4 * 2, 5 * 2)),))

    def test_negative_integer_tuples(self):
        """Test negative integer tuples"""
        self.assertEqual(index_multiplication((-1, 2), (-3, 4)), ((-3 * -1, 4 * 2),))
        self.assertEqual(index_multiplication(((1, -2)), ((-3, 4))) , (((-3 * 1, 4 * -2)),))

    def test_floats_tuples(self):
        """Test floats tuples"""
        self.assertAlmostEqual(index_multiplication((1.5, 2), (3, 4)), ((3 * 1.5, 4 * 2), 0.01))
        self.assertAlmostEqual(index_multiplication(((1.5, 2)), ((3, 4))) , (((3 * 1.5, 4 * 2)), 0.01))

    def test_mixed_types_tuples(self):
        """Test mixed types tuples"""
        self.assertRaises(TypeError, index_multiplication, ((1, 'a'), (3, 4)))
