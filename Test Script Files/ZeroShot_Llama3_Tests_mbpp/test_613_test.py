import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(maximum_value([]), [])

    def test_single_element_list(self):
        self.assertEqual(maximum_value([[(1, [1])]]), [(1, 1)])

    def test_multiple_elements_list(self):
        self.assertEqual(maximum_value([[(1, [1, 2, 3]), (2, [4, 5, 6])]]), [(1, 3), (2, 6)])

    def test_list_with_duplicates(self):
        self.assertEqual(maximum_value([[(1, [1, 2, 2, 3]), (2, [4, 5, 5, 6])]]), [(1, 3), (2, 6)])

    def test_list_with_negative_numbers(self):
        self.assertEqual(maximum_value([[(1, [-1, 0, 1]), (2, [-2, 0, 2])]]), [(1, 1), (2, 2)])

    def test_list_with_zero(self):
        self.assertEqual(maximum_value([[(1, [0, 1, 2]), (2, [0, 3, 4])]]), [(1, 2), (2, 4)])
