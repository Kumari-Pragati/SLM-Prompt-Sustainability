import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_empty_tuples(self):
        """Test concatenating empty tuples"""
        self.assertEqual(concatenate_nested((), ()), ())

    def test_single_element_tuples(self):
        """Test concatenating tuples with a single element"""
        self.assertEqual(concatenate_nested((1), (2)), (1, 2))
        self.assertEqual(concatenate_nested(('a'), (1, 'b', 'c')), ('a', 1, 'b', 'c'))

    def test_multiple_element_tuples(self):
        """Test concatenating tuples with multiple elements"""
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))
        self.assertEqual(concatenate_nested(('a', 'b'), (1, 'c', 'd')), ('a', 'b', 1, 'c', 'd'))

    def test_mixed_types(self):
        """Test concatenating tuples with mixed types"""
        self.assertEqual(concatenate_nested((1, 'a'), (2, 'b', 3)), (1, 'a', 2, 'b', 3))

    def test_nested_tuples(self):
        """Test concatenating tuples with nested tuples"""
        self.assertEqual(concatenate_nested((1, (2, 3)), ((4, 5), 6)), (1, 2, 3, 4, 5, 6))
        self.assertEqual(concatenate_nested(('a', (1, 'b')), (('c',), 2, ('d', 'e'))), ('a', 1, 'b', 'c', 2, 'd', 'e'))

    def test_empty_list_as_input(self):
        """Test handling empty list as input"""
        with self.assertRaises(TypeError):
            concatenate_nested((1, 2), [])

    def test_list_as_input(self):
        """Test handling list as input"""
        with self.assertRaises(TypeError):
            concatenate_nested([1, 2], ())
