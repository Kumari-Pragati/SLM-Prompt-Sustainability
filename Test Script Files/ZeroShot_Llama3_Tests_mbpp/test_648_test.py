import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):

    def test_exchange_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6]), [1, 2, 4, 3, 5, 6])
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [1, 2, 4, 3, 5])
        self.assertEqual(exchange_elements([1, 2, 3]), [1, 2, 3])
        self.assertEqual(exchange_elements([]), [])
        self.assertEqual(exchange_elements([1]), [1])
        self.assertEqual(exchange_elements([1, 2]), [1, 2])

    def test_exchange_elements_with_odd_length(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 4, 3, 6, 5, 8, 7, 10, 9])

    def test_exchange_elements_with_empty_list(self):
        self.assertEqual(exchange_elements([]), [])

    def test_exchange_elements_with_single_element(self):
        self.assertEqual(exchange_elements([1]), [1])

    def test_exchange_elements_with_two_elements(self):
        self.assertEqual(exchange_elements([1, 2]), [1, 2])

    def test_exchange_elements_with_three_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3]), [1, 2, 3])

    def test_exchange_elements_with_four_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4]), [1, 2, 4, 3])

    def test_exchange_elements_with_five_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [1, 2, 4, 3, 5])

    def test_exchange_elements_with_six_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6]), [1, 2, 4, 3, 5, 6])

    def test_exchange_elements_with_seven_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6, 7]), [1, 2, 4, 3, 6, 5, 7])

    def test_exchange_elements_with_eight_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 4, 3, 6, 5, 8, 7])

    def test_exchange_elements_with_nine_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 4, 3, 6, 5, 8, 7, 9])

    def test_exchange_elements_with_ten_elements(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 4, 3, 6, 5, 8, 7, 10, 9])
