import unittest
from mbpp_105_code import count

class TestCountFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(count([1, -2, 3]), 4)

    def test_floats(self):
        self.assertAlmostEqual(count([1.0, 2.0, 3.0]), 6.0)

    def test_mixed_types(self):
        self.assertEqual(count([1, '2', 3]), 6)

    def test_list_with_none(self):
        self.assertEqual(count([1, None, 3]), 4)
