import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_rear((['a', 'b', 'c'], [1, 2, 3])), ['c', 3])

    def test_empty_list(self):
        self.assertEqual(extract_rear(([], [])), ([], []))

    def test_single_element(self):
        self.assertEqual(extract_rear((['a'], [1])), ['a', 1])

    def test_mixed_types(self):
        self.assertEqual(extract_rear((['a', 1], [2, 'b'])), [1, 'b'])

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            extract_rear((1, 2, 3))
        with self.assertRaises(TypeError):
            extract_rear((['a', 'b', 'c'], '123'))
