import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertIsInstance(substract_elements((), ()), tuple)
        self.assertListEqual(substract_elements((), ()), [])

    def test_single_element_tuples(self):
        self.assertIsInstance(substract_elements((1,), (1,)), tuple)
        self.assertListEqual(substract_elements((1,), (1,)), [0])

    def test_different_length_tuples(self):
        self.assertIsInstance(substract_elements((1, 2, 3), (4, 5)), tuple)
        self.assertListEqual(substract_elements((1, 2, 3), (4, 5)), [-3, -3, 1])

    def test_negative_numbers(self):
        self.assertIsInstance(substract_elements((-1, 2, -3), (4, -5)), tuple)
        self.assertListEqual(substract_elements((-1, 2, -3), (4, -5)), [5, 7, 2])
