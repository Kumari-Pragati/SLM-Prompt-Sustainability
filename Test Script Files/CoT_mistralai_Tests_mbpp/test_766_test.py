import unittest
from mbpp_766_code import pair_wise

class TestPairWise(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(pair_wise([]), [])

    def test_single_element_list(self):
        self.assertListEqual(pair_wise([1]), [(1, None)])

    def test_normal_list(self):
        self.assertListEqual(pair_wise([1, 2, 3, 4]), [(1, 2), (2, 3), (3, 4)])

    def test_list_with_last_element_removed(self):
        self.assertListEqual(pair_wise([1, 2, 3]), [(1, 2), (2, 3)])

    def test_list_with_duplicates(self):
        self.assertListEqual(pair_wise([1, 1, 2, 2, 3]), [(1, 1), (1, 2), (2, 2), (2, 3)])

    def test_list_with_negative_numbers(self):
        self.assertListEqual(pair_wise([-1, 0, 1]), [(-1, 0), (0, 1)])

    def test_list_with_floats(self):
        self.assertListEqual(pair_wise([1.0, 2.0, 3.0]), [(1.0, 2.0), (2.0, 3.0)])

    def test_list_with_mixed_types(self):
        self.assertRaises(TypeError, pair_wise, [1, "two", 3])
