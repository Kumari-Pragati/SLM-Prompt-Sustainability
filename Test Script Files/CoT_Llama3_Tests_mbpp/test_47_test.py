import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):
    def test_equal_A_and_B(self):
        self.assertEqual(compute_Last_Digit(10, 10), 1)

    def test_B_greater_than_A_by_5(self):
        self.assertEqual(compute_Last_Digit(10, 15), 0)

    def test_B_greater_than_A_by_4(self):
        self.assertEqual(compute_Last_Digit(10, 14), 4)

    def test_B_greater_than_A_by_3(self):
        self.assertEqual(compute_Last_Digit(10, 13), 6)

    def test_B_greater_than_A_by_2(self):
        self.assertEqual(compute_Last_Digit(10, 12), 2)

    def test_B_greater_than_A_by_1(self):
        self.assertEqual(compute_Last_Digit(10, 11), 0)

    def test_B_greater_than_A_by_0(self):
        self.assertEqual(compute_Last_Digit(10, 10), 1)

    def test_A_greater_than_B(self):
        self.assertEqual(compute_Last_Digit(15, 10), 0)

    def test_A_and_B_negative(self):
        self.assertEqual(compute_Last_Digit(-10, -10), 1)

    def test_A_and_B_zero(self):
        self.assertEqual(compute_Last_Digit(0, 0), 1)

    def test_A_and_B_non_integer(self):
        with self.assertRaises(TypeError):
            compute_Last_Digit(10.5, 10)
