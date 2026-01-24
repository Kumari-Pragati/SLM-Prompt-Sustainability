import unittest
from mbpp_673_code import convert

class TestConvert(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(convert([1, 2, 3]), 6)
        self.assertEqual(convert([0, 0, 0]), 0)
        self.assertEqual(convert([9, 9, 9]), 729)

    def test_edge_cases(self):
        self.assertEqual(convert([-1, 2, 3]), 111)
        self.assertEqual(convert([10, 20, 30]), 63010)
        self.assertEqual(convert([-10, -20, -30]), 3086080)
        self.assertEqual(convert([0, -1, 0]), 0)
        self.assertEqual(convert([0, 0, -1]), 0)
        self.assertEqual(convert([-1, 0, 0]), 0)

    def test_complex(self):
        self.assertEqual(convert([100, 200, 300]), 600300)
        self.assertEqual(convert([-100, -200, -300]), 3086080)
        self.assertEqual(convert([100, -200, 300]), 100600300)
        self.assertEqual(convert([-100, 200, -300]), -3086080)
        self.assertEqual(convert([-100, -200, 300]), -3086080)
        self.assertEqual(convert([-100, 200, 300, 400]), -13086080)
