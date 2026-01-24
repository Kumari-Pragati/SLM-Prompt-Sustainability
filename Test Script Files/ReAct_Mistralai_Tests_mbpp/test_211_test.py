import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):

    def test_base_case(self):
        """Test that the function correctly returns 1 for input 1."""
        self.assertEqual(count_Num(1), 1)

    def test_positive_integer(self):
        """Test that the function correctly counts numbers greater than 1."""
        for n in range(2, 10):
            self.assertEqual(count_Num(n), pow(2, n - 2))

    def test_zero(self):
        """Test that the function correctly returns 0 for input 0."""
        self.assertEqual(count_Num(0), 0)

    def test_negative_integer(self):
        """Test that the function correctly returns 0 for input less than 0."""
        for n in range(-1, -10, -1):
            self.assertEqual(count_Num(n), 0)

    def test_floats(self):
        """Test that the function correctly handles non-integer inputs."""
        for n in [1.0, 2.5, -3.14]:
            with self.assertRaises(TypeError):
                count_Num(n)
