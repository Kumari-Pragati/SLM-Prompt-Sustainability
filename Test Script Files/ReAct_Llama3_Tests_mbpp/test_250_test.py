import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(count_X((), 5), 0)

    def test_no_x_in_tuple(self):
        self.assertEqual(count_X((1, 2, 3), 5), 0)

    def test_x_in_tuple(self):
        self.assertEqual(count_X((1, 2, 3, 5, 5), 5), 2)

    def test_x_at_start(self):
        self.assertEqual(count_X((5, 1, 2, 3), 5), 1)

    def test_x_at_end(self):
        self.assertEqual(count_X((1, 2, 3, 5), 5), 1)

    def test_x_in_middle(self):
        self.assertEqual(count_X((1, 5, 2, 3, 5), 5), 2)

    def test_x_multiple_times(self):
        self.assertEqual(count_X((1, 5, 5, 2, 3, 5, 5), 5), 4)

    def test_x_not_in_tuple(self):
        with self.assertRaises(TypeError):
            count_X(None, 5)

    def test_non_integer_x(self):
        with self.assertRaises(TypeError):
            count_X((1, 2, 3), '5')
