import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(maximize_elements((), ()), ())

    def test_single_element_lists(self):
        self.assertEqual(maximize_elements((1,), (2,)), (1,))
        self.assertEqual(maximize_elements((2,), (1,)), (2,))

    def test_equal_length_lists(self):
        self.assertEqual(maximize_elements((1, 2, 3), (4, 5, 6)), (4, 5, 6))
        self.assertEqual(maximize_elements((4, 5, 6), (1, 2, 3)), (4, 5, 6))

    def test_different_length_lists(self):
        self.assertEqual(maximize_elements((1, 2, 3), (4, 5)), (4, 5))
        self.assertEqual(maximize_elements((4, 5), (1, 2, 3)), (4, 5))

    def test_negative_numbers(self):
        self.assertEqual(maximize_elements((-1, 2), (-3, 4)), (2, 4))
        self.assertEqual(maximize_elements((-3, 4), (-1, 2)), (4, 2))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            maximize_elements('1', '2')
        with self.assertRaises(TypeError):
            maximize_elements([1, 2], 3)
        with self.assertRaises(TypeError):
            maximize_elements(1, [1, 2])
