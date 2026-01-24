import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(average_tuple([]), [])

    def test_single_element_list(self):
        self.assertAlmostEqual(average_tuple([[1]]), [1.0])

    def test_multiple_element_lists(self):
        self.assertListEqual(average_tuple([[1, 2], [3, 4], [5, 6]]), [2.0, 4.0, 5.0])

    def test_mixed_type_elements(self):
        self.assertRaises(TypeError, average_tuple, [[1, 2], [3, "4"], [5, 6]])

    def test_negative_numbers(self):
        self.assertAlmostEqual(average_tuple([[-1, 2], [3, -4], [-5, 6]]), [-0.5, 1.5, 1.5])
