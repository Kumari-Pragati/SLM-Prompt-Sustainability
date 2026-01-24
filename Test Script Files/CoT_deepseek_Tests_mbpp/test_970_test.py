import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_of_two(3, 5), 3)
        self.assertEqual(min_of_two(7, 2), 2)

    def test_same_values(self):
        self.assertEqual(min_of_two(4, 4), 4)

    def test_negative_numbers(self):
        self.assertEqual(min_of_two(-3, -1), -3)
        self.assertEqual(min_of_two(-7, -2), -7)

    def test_boundary_conditions(self):
        self.assertEqual(min_of_two(0, 1), 0)
        self.assertEqual(min_of_two(1, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_of_two("3", 5)
        with self.assertRaises(TypeError):
            min_of_two(3, "5")
        with self.assertRaises(TypeError):
            min_of_two("3", "5")
