import unittest
from mbpp_648_code import exchange_elements

class TestExchangeElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5])
        self.assertEqual(exchange_elements([0, 1, 2, 3, 4]), [1, 0, 3, 2, 4])
        self.assertEqual(exchange_elements([6, 7, 8, 9]), [7, 6, 9, 8])

    def test_edge_cases(self):
        self.assertEqual(exchange_elements([]), [])
        self.assertEqual(exchange_elements([1]), [1])
        self.assertEqual(exchange_elements([1, 2]), [2, 1])
        self.assertEqual(exchange_elements([1, 2, 3]), [2, 1, 3])

    def test_boundary_cases(self):
        self.assertEqual(exchange_elements([0, 1, 2, 3, 4, 5]), [1, 0, 3, 2, 5, 4])
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6]), [2, 1, 4, 3, 6, 5])
        self.assertEqual(exchange_elements([1, 2, 3, 4, 5, 6, 7]), [2, 1, 4, 3, 6, 5, 7])
