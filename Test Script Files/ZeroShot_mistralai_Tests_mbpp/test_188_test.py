import unittest
from mbpp_188_code import datetime
from 188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    def setUp(self):
        self.start_time = datetime.now()

    def test_prod_square_positive(self):
        test_cases = [(3, True), (4, True), (9, True), (10, True), (12, True), (16, True), (20, True), (25, True), (28, True), (36, True)]
        for test_case in test_cases:
            self.assertEqual(prod_Square(test_case[0]), test_case[1])

    def test_prod_square_negative(self):
        test_cases = [(1, False), (2, False), (5, False), (6, False), (7, False), (8, False), (11, False), (13, False), (14, False), (17, False)]
        for test_case in test_cases:
            self.assertFalse(prod_Square(test_case[0]))

    def test_prod_square_edge_cases(self):
        test_cases = [(0, False), (15, False), (27, False), (29, False), (35, False)]
        for test_case in test_cases:
            self.assertFalse(prod_Square(test_case[0]))

    def tearDown(self):
        print(f"Test {self.__class__.__name__} took {datetime.now() - self.start_time} seconds to complete.")
