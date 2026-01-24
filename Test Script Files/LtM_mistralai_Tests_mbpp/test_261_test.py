import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_simple_division(self):
        self.assertEqual(division_elements((1, 2, 3), (2, 2, 2)), (0, 1, 1))
        self.assertEqual(division_elements((4, 4, 4), (2, 2, 2)), (1, 2, 2))

    def test_division_with_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: division_elements((1, 0), (1,)))
        self.assertRaises(ZeroDivisionError, lambda: division_elements((0, 1), (1,)))

    def test_mixed_types(self):
        self.assertRaises(TypeError, lambda: division_elements((1, '2'), (2,)))
        self.assertRaises(TypeError, lambda: division_elements((1,), (2, '2')))

    def test_empty_inputs(self):
        self.assertIsNone(division_elements((), ()))
        self.assertIsNone(division_elements((1,), ()))
        self.assertIsNone(division_elements((), (1,)))
