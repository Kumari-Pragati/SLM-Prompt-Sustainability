import unittest

from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5), 1)

    def test_edge_case(self):
        self.assertEqual(count_element_in_list([], 5), 0)

    def test_corner_case(self):
        self.assertEqual(count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_element_in_list("not a list", 5)
