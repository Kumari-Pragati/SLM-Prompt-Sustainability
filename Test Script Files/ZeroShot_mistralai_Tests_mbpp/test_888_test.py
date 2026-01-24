import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertEqual(substract_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(substract_elements((1,), (2,)), ((-1,)))
        self.assertEqual(substract_elements((2,), (1,)), ((-1,)))

    def test_multiple_element_tuples(self):
        self.assertEqual(substract_elements((1, 2, 3), (2, 3, 4)), ((-1, 1, 3)))
        self.assertEqual(substract_elements((2, 3, 4), (1, 2, 3)), ((-1, -1, 1)))
