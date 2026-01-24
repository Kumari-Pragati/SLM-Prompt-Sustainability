import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(inversion_elements([]), ())

    def test_single_element(self):
        self.assertEqual(inversion_elements((1,)), ((0,)))
        self.assertEqual(inversion_elements((0,)), ((1,)))

    def test_multiple_elements(self):
        self.assertEqual(inversion_elements((1, 0, 1, 0, 1)), ((0, 1, 0, 1, 0)))
        self.assertEqual(inversion_elements((0, 1, 0, 1, 0)), ((1, 0, 1, 0, 1)))
