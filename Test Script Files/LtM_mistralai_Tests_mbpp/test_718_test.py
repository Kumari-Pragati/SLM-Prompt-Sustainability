import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3])
        self.assertListEqual(alternate_elements([6, 7, 8, 9, 10]), [6, 8])

    def test_edge_cases(self):
        self.assertListEqual(alternate_elements([]), [])
        self.assertListEqual(alternate_elements([1]), [1])
        self.assertListEqual(alternate_elements([1, 1]), [1])

    def test_complex(self):
        self.assertListEqual(alternate_elements([0, 1, 2, 3, 4, 5, 6]), [0, 2, 4, 6])
        self.assertListEqual(alternate_elements([10, 11, 12, 13, 14, 15, 16]), [10, 12, 14])
        self.assertListEqual(alternate_elements([-1, 0, 1, -2, 3]), [-1, 1, -2])
