import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_substract_elements_positive(self):
        self.assertTupleEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-4, -3, -3)))
        self.assertTupleEqual(substract_elements((0, 0, 0), (1, 2, 3)), ((-1, -2, -3)))
        self.assertTupleEqual(substract_elements((4, 5, 6), (0, 0, 0)), ((4, 5, 6)))

    def test_substract_elements_empty_lists(self):
        self.assertIsNone(substract_elements((), ()))
        self.assertIsNone(substract_elements((1,), ()))
        self.assertIsNone(substract_elements((), (1,)))

    def test_substract_elements_different_lengths(self):
        self.assertRaises(ValueError, substract_elements, ((1, 2, 3), (1, 2)))
        self.assertRaises(ValueError, substract_elements, ((1, 2), (1, 2, 3)))

    def test_substract_elements_non_tuple_inputs(self):
        self.assertRaises(TypeError, substract_elements, (1, 2), [3, 4])
        self.assertRaises(TypeError, substract_elements, [1, 2], (3, 4))
