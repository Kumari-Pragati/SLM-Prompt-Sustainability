import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximize_elements((1, 2, 3), (4, 5, 6)), ((1, 5, 6)))
        self.assertEqual(maximize_elements((-1, 0, 1), (2, 3, 4)), ((1, 3, 4)))
        self.assertEqual(maximize_elements((5, 4, 3), (2, 1, 0)), ((5, 4, 1)))

    def test_edge_case_empty_lists(self):
        self.assertEqual(maximize_elements((), ()), ())
        self.assertEqual(maximize_elements((1,), ()), ((1,)))
        self.assertEqual(maximize_elements((), (1,)), ((1,)))

    def test_edge_case_single_element(self):
        self.assertEqual(maximize_elements((1,), (2,)), ((2,)))
        self.assertEqual(maximize_elements((2,), (1,)), ((2,)))

    def test_corner_case_different_lengths(self):
        self.assertEqual(maximize_elements((1, 2), (3, 4, 5)), ((1, 4)))
        self.assertEqual(maximize_elements((3, 4, 5), (1, 2)), ((5, 2)))
