import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_empty_list(self):
        """Test for an empty list"""
        self.assertEqual(bell_Number(0), 1)

    def test_single_element_list(self):
        """Test for a list with a single element"""
        self.assertEqual(bell_Number(1), 1)

    def test_small_list(self):
        """Test for a small list"""
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(3), 4)
        self.assertEqual(bell_Number(4), 10)

    def test_large_list(self):
        """Test for a large list"""
        self.assertEqual(bell_Number(10), 514)
        self.assertEqual(bell_Number(20), 19749)

    def test_negative_input(self):
        """Test for negative input"""
        with self.assertRaises(ValueError):
            bell_Number(-1)

    def test_float_input(self):
        """Test for float input"""
        with self.assertRaises(TypeError):
            bell_Number(3.5)

    def test_string_input(self):
        """Test for string input"""
        with self.assertRaises(TypeError):
            bell_Number('abc')
