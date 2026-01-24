import unittest
from mbpp_509_code import average_Odd

class TestAverageOdd(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(average_Odd(10), 5)

    def test_edge_case(self):
        self.assertEqual(average_Odd(0), -1)

    def test_edge_case2(self):
        self.assertEqual(average_Odd(1), -1)

    def test_edge_case3(self):
        self.assertEqual(average_Odd(2), 1)

    def test_edge_case4(self):
        self.assertEqual(average_Odd(4), 2)

    def test_edge_case5(self):
        self.assertEqual(average_Odd(6), 3)

    def test_edge_case6(self):
        self.assertEqual(average_Odd(8), 4)

    def test_edge_case7(self):
        self.assertEqual(average_Odd(10), 5)

    def test_edge_case8(self):
        self.assertEqual(average_Odd(12), 6)

    def test_edge_case9(self):
        self.assertEqual(average_Odd(14), 7)

    def test_edge_case10(self):
        self.assertEqual(average_Odd(16), 8)

    def test_invalid_input(self):
        self.assertEqual(average_Odd(3), "Invalid Input")

    def test_invalid_input2(self):
        self.assertEqual(average_Odd(5), "Invalid Input")

    def test_invalid_input3(self):
        self.assertEqual(average_Odd(7), "Invalid Input")

    def test_invalid_input4(self):
        self.assertEqual(average_Odd(9), "Invalid Input")

    def test_invalid_input5(self):
        self.assertEqual(average_Odd(11), "Invalid Input")

    def test_invalid_input6(self):
        self.assertEqual(average_Odd(13), "Invalid Input")

    def test_invalid_input7(self):
        self.assertEqual(average_Odd(15), "Invalid Input")

    def test_invalid_input8(self):
        self.assertEqual(average_Odd(17), "Invalid Input")
