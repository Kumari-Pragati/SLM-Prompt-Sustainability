import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])

    def test_single_element_input(self):
        self.assertEqual(pair_wise([1]), [(1, None)])

    def test_empty_input(self):
        self.assertEqual(pair_wise([]), [])

    def test_negative_numbers(self):
        self.assertEqual(pair_wise([-1, -2, -3]), [(-1, -2), (-2, -3)])

    def test_mixed_types(self):
        self.assertEqual(pair_wise([1, 'a', 3]), [(1, 'a'), ('a', 3)])

    def test_duplicate_elements(self):
        self.assertEqual(pair_wise([1, 1, 2, 3]), [(1, 1), (1, 2), (2, 3)])
