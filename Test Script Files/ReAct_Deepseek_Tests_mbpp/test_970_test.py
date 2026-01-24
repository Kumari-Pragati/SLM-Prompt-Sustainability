import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_of_two(3, 5), 3)
        self.assertEqual(min_of_two(7, 2), 2)

    def test_edge_cases(self):
        self.assertEqual(min_of_two(0, 0), 0)
        self.assertEqual(min_of_two(-1, -2), -2)
        self.assertEqual(min_of_two(float('inf'), float('inf')), float('inf'))

    def test_explicitly_handled_error_cases(self):
        # Since the function only takes two arguments, passing more than two arguments should raise a TypeError
        with self.assertRaises(TypeError):
            min_of_two(1, 2, 3)

        # The arguments should be numbers, not strings. If they are strings, the function should return the first argument
        self.assertEqual(min_of_two('3', '5'), '3')
