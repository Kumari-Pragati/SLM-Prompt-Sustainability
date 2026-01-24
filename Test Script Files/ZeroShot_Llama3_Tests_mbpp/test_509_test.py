import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):

    def test_average_Odd_valid_input(self):
        self.assertEqual(average_Odd(10), 5)

    def test_average_Odd_invalid_input_even(self):
        self.assertEqual(average_Odd(10), "Invalid Input")

    def test_average_Odd_invalid_input_negative(self):
        self.assertEqual(average_Odd(-10), "Invalid Input")

    def test_average_Odd_invalid_input_zero(self):
        self.assertEqual(average_Odd(0), "Invalid Input")

    def test_average_Odd_invalid_input_one(self):
        self.assertEqual(average_Odd(1), "Invalid Input")

    def test_average_Odd_invalid_input_two(self):
        self.assertEqual(average_Odd(2), "Invalid Input")

    def test_average_Odd_invalid_input_three(self):
        self.assertEqual(average_Odd(3), "Invalid Input")

    def test_average_Odd_invalid_input_four(self):
        self.assertEqual(average_Odd(4), "Invalid Input")

    def test_average_Odd_invalid_input_five(self):
        self.assertEqual(average_Odd(5), "Invalid Input")

    def test_average_Odd_invalid_input_six(self):
        self.assertEqual(average_Odd(6), "Invalid Input")

    def test_average_Odd_invalid_input_seven(self):
        self.assertEqual(average_Odd(7), 4)

    def test_average_Odd_invalid_input_eight(self):
        self.assertEqual(average_Odd(8), "Invalid Input")

    def test_average_Odd_invalid_input_nine(self):
        self.assertEqual(average_Odd(9), "Invalid Input")

    def test_average_Odd_invalid_input_ten(self):
        self.assertEqual(average_Odd(10), "Invalid Input")

    def test_average_Odd_invalid_input_eleven(self):
        self.assertEqual(average_Odd(11), 6)

    def test_average_Odd_invalid_input_twelve(self):
        self.assertEqual(average_Odd(12), "Invalid Input")

    def test_average_Odd_invalid_input_thirteen(self):
        self.assertEqual(average_Odd(13), 7)

    def test_average_Odd_invalid_input_fourteen(self):
        self.assertEqual(average_Odd(14), "Invalid Input")

    def test_average_Odd_invalid_input_fifteen(self):
        self.assertEqual(average_Odd(15), 8)

    def test_average_Odd_invalid_input_sixteen(self):
        self.assertEqual(average_Odd(16), "Invalid Input")

    def test_average_Odd_invalid_input_seventeen(self):
        self.assertEqual(average_Odd(17), 9)

    def test_average_Odd_invalid_input_eighteen(self):
        self.assertEqual(average_Odd(18), "Invalid Input")

    def test_average_Odd_invalid_input_nineteen(self):
        self.assertEqual(average_Odd(19), 10)

    def test_average_Odd_invalid_input_twenty(self):
        self.assertEqual(average_Odd(20), "Invalid Input")
