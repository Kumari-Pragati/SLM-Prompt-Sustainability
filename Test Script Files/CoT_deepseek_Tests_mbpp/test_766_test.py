import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])

    def test_single_element(self):
        self.assertEqual(pair_wise([1]), [])

    def test_empty_list(self):
        self.assertEqual(pair_wise([]), [])

    def test_negative_numbers(self):
        self.assertEqual(pair_wise([-1, -2, -3, -4]), [(-1, -2), (-2, -3), (-3, -4)])

    def test_zero(self):
        self.assertEqual(pair_wise([0, 1, 2, 3]), [(0, 1), (1, 2), (2, 3)])

    def test_large_numbers(self):
        self.assertEqual(pair_wise([100, 200, 300, 400]), [(100, 200), (200, 300), (300, 400)])

    def test_non_integer_elements(self):
        self.assertEqual(pair_wise([1.1, 2.2, 3.3, 4.4]), [(1.1, 2.2), (2.2, 3.3), (3.3, 4.4)])

    def test_string_elements(self):
        self.assertEqual(pair_wise(['a', 'b', 'c', 'd']), [('a', 'b'), ('b', 'c'), ('c', 'd')])

    def test_mixed_elements(self):
        self.assertEqual(pair_wise([1, 'a', 2, 'b']), [(1, 'a'), ('a', 2)])
