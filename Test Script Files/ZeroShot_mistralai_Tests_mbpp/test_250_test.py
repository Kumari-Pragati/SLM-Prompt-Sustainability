import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_X([], 'x'), 0)

    def test_single_element(self):
        self.assertEqual(count_X(['x'], 'x'), 1)
        self.assertEqual(count_X(['X'], 'x'), 1)

    def test_multiple_elements(self):
        self.assertEqual(count_X(['x', 'y', 'x', 'z', 'x'], 'x'), 4)
        self.assertEqual(count_X(['X', 'Y', 'x', 'Z', 'x'], 'x'), 3)

    def test_case_insensitive(self):
        self.assertEqual(count_X(['x', 'y', 'X', 'z', 'x'], 'x'), 4)
        self.assertEqual(count_X(['X', 'y', 'x', 'Z', 'x'], 'x'), 3)

    def test_non_matching_element(self):
        self.assertEqual(count_X(['x', 'y', 'z'], 'x'), 1)
        self.assertEqual(count_X(['X', 'Y', 'z'], 'x'), 1)
        self.assertEqual(count_X(['x', 'y', 'z'], 'Y'), 0)
        self.assertEqual(count_X(['X', 'Y', 'z'], 'Y'), 1)
