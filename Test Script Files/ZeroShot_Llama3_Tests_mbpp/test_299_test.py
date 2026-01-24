import unittest
from mbpp_299_code import max_aggregate

class TestMaxAggregate(unittest.TestCase):

    def test_max_aggregate(self):
        stdata = [('Alice', 90), ('Bob', 80), ('Alice', 70)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 160))

        stdata = [('Alice', 90), ('Bob', 80), ('Charlie', 70)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 90))

        stdata = [('Alice', 90), ('Bob', 80), ('Charlie', 70), ('Alice', 70)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 160))

        stdata = [('Alice', 90), ('Bob', 80), ('Charlie', 70), ('Alice', 70), ('Bob', 80)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 160))

        stdata = [('Alice', 90), ('Bob', 80), ('Charlie', 70), ('Alice', 70), ('Bob', 80), ('Charlie', 70)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 160))

        stdata = [('Alice', 90), ('Bob', 80), ('Charlie', 70), ('Alice', 70), ('Bob', 80), ('Charlie', 70), ('Alice', 90)]
        self.assertEqual(max_aggregate(stdata), ('Alice', 250))
