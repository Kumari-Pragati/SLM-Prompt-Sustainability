import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_empty_tuple(self):
        """Test if function returns 0 for an empty tuple"""
        self.assertEqual(count_X((), 'x'), 0)

    def test_single_element_tuple(self):
        """Test if function returns 1 for a single element tuple"""
        self.assertEqual(count_X(('x',), 'x'), 1)

    def test_multiple_elements_same_x(self):
        """Test if function correctly counts multiple occurrences of x"""
        self.assertEqual(count_X(('x', 'y', 'x', 'z', 'x'), 'x'), 3)

    def test_multiple_elements_different_x(self):
        """Test if function returns 0 for a tuple with no x"""
        self.assertEqual(count_X(('a', 'b', 'c', 'd'), 'x'), 0)

    def test_mixed_case_x(self):
        """Test if function correctly counts mixed case X"""
        self.assertEqual(count_X(('x', 'X', 'x'), 'x'), 2)

    def test_none_type_input(self):
        """Test if function correctly handles None as input"""
        self.assertRaises(TypeError, count_X, None, 'x')

    def test_string_input(self):
        """Test if function correctly handles string as input"""
        self.assertRaises(TypeError, count_X, 'test', 'x')
