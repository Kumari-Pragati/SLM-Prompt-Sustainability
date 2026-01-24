import unittest
from904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_even_num_positive(self):
        self.assertTrue(even_num(0))
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(100))

    def test_even_num_negative(self):
        self.assertFalse(even_num(-1))
        self.assertFalse(even_num(-2))
        self.assertFalse(even_num(-100))

    def test_edge_cases(self):
        self.assertTrue(even_num(1))
        self.assertTrue(even_num(2147483648))  # Maximum positive integer
        self.assertFalse(even_num(-2147483649))  # Minimum negative integer

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, even_num, 3.14)
        self.assertRaises(TypeError, even_num, [1, 2, 3])
        self.assertRaises(TypeError, even_num, (1, 2, 3))
        self.assertRaises(TypeError, even_num, None)
        self.assertRaises(TypeError, even_num, True)
        self.assertRaises(TypeError, even_num, False)
