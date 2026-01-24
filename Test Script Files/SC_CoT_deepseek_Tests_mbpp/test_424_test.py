import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_rear((['a', 'b', 'c'], [1, 2, 3])), ['c', 3])

    def test_empty_tuple(self):
        self.assertEqual(extract_rear(()), [])

    def test_single_element_tuple(self):
        self.assertEqual(extract_rear((['a'],)), ['a'])

    def test_mixed_types(self):
        self.assertEqual(extract_rear(([1, 2, 3], ['a', 'b', 'c'])), [3, 'c'])

    def test_nested_tuple(self):
        self.assertEqual(extract_rear((([1, 2, 3], [4, 5, 6]), ([7, 8, 9], [10, 11, 12]))), 
                         [[3, 6], [9, 12]])

    def test_empty_sublists(self):
        self.assertEqual(extract_rear(([], []), []))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_rear(123)
