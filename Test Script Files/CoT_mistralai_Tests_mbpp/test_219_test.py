import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsInstance(extract_min_max((), 0), tuple)
        self.assertIsNone(extract_min_max((), 1))

    def test_single_element(self):
        self.assertEqual(extract_min_max((1,), 0), (1,))
        self.assertEqual(extract_min_max((1,), 1), (1,))

    def test_multiple_elements(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4), 2), (1, 2, 3))
        self.assertEqual(extract_min_max((1, 2, 3, 4), 0), (1, 2, 3, 4))
        self.assertEqual(extract_min_max((1, 2, 3, 4), 3), (2, 3, 4))

    def test_negative_index(self):
        self.assertIsNone(extract_min_max((1, 2, 3, 4), -1))
        self.assertIsNone(extract_min_max((1, 2, 3, 4), -2))

    def test_invalid_input(self):
        self.assertRaises(TypeError, extract_min_max, 'invalid input', 0)
        self.assertRaises(TypeError, extract_min_max, (1, 'invalid input'), 0)
        self.assertRaises(TypeError, extract_min_max, (1, 2, 3, 4), -2)
        self.assertRaises(TypeError, extract_min_max, (1, 2, 3, 4), -1)
        self.assertRaises(ValueError, extract_min_max, (), -1)
        self.assertRaises(ValueError, extract_min_max, (), 0)
