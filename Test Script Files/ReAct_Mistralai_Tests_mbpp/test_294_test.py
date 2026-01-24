import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_empty_list(self):
        """Test max_val with an empty list"""
        with self.assertRaises(TypeError):
            max_val([])

    def test_single_integer(self):
        """Test max_val with a single integer"""
        result = max_val([42])
        self.assertEqual(result, 42)

    def test_multiple_integers(self):
        """Test max_val with multiple integers"""
        result = max_val([42, 17, -3, 99])
        self.assertEqual(result, 99)

    def test_mixed_types(self):
        """Test max_val with a list containing integers and non-integers"""
        with self.assertRaises(TypeError):
            max_val([42, 'string', 17, None])

    def test_negative_numbers(self):
        """Test max_val with negative numbers"""
        result = max_val([-42, -17, 3, -99])
        self.assertEqual(result, -42)

    def test_floats(self):
        """Test max_val with floats"""
        result = max_val([42.0, 3.14, -1.0])
        self.assertEqual(result, 42.0)
