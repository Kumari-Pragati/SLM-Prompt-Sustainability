import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_recursive(self):
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)

    def test_edge(self):
        self.assertRaisesRecursionError(lambda: sequence(100))

    def test_edge2(self):
        self.assertEqual(sequence(1), 1)

    def test_edge3(self):
        self.assertEqual(sequence(2), 1)

    def test_edge4(self):
        self.assertEqual(sequence(3), 2)

    def test_edge5(self):
        self.assertRaisesRecursionError(lambda: sequence(1000))

    def test_edge6(self):
        self.assertRaisesRecursionError(lambda: sequence(-1))

    def test_edge7(self):
        self.assertRaisesRecursionError(lambda: sequence(0))

    def test_edge8(self):
        self.assertRaisesRecursionError(lambda: sequence(-100))

    def test_edge9(self):
        self.assertRaisesRecursionError(lambda: sequence(1000))

    def test_edge10(self):
        self.assertRaisesRecursionError(lambda: sequence(-1000))

    def test_edge11(self):
        self.assertRaisesRecursionError(lambda: sequence(10000))

    def test_edge12(self):
        self.assertRaisesRecursionError(lambda: sequence(-10000))

    def test_edge13(self):
        self.assertRaisesRecursionError(lambda: sequence(100000))

    def test_edge14(self):
        self.assertRaisesRecursionError(lambda: sequence(-100000))

    def test_edge15(self):
        self.assertRaisesRecursionError(lambda: sequence(1000000))

    def test_edge16(self):
        self.assertRaisesRecursionError(lambda: sequence(-1000000))

    def test_edge17(self):
        self.assertRaisesRecursionError(lambda: sequence(10000000))

    def test_edge18(self):
        self.assertRaisesRecursionError(lambda: sequence(-10000000))

    def test_edge19(self):
        self.assertRaisesRecursionError(lambda: sequence(100000000))

    def test_edge20(self):
        self.assertRaisesRecursionError(lambda: sequence(-100000000))

    def test_edge21(self):
        self.assertRaisesRecursionError(lambda: sequence(1000000000))

    def test_edge22(self):
        self.assertRaisesRecursionError(lambda: sequence(-1000000000))

    def test_edge23(self):
        self.assertRaisesRecursionError(lambda: sequence(10000000000))

    def test_edge24(self):
        self.assertRaisesRecursionError(lambda: sequence(-10000000000))

    def test_edge25(self):
        self.assertRaisesRecursionError(lambda: sequence(100000000000))

    def test_edge26(self):
        self.assertRaisesRecursionError(lambda: sequence(-100000000000))

    def test_edge27(self):
        self.assertRaisesRecursionError(lambda: sequence(1000000000000))

    def test_edge28(self):
        self.assertRaisesRecursionError(lambda: sequence(-1000000000000))

    def test_edge29(self):
        self.assertRaisesRecursionError(lambda: sequence(10000000000000))

    def test_edge30(self):
        self.assertRaisesRecursionError(lambda: sequence(-10000000000000))

    def test_edge31(self):
        self.assertRaisesRecursionError(lambda: sequence(100000000000000))

    def test_edge32(self):
        self.assertRaisesRecursionError(lambda: sequence(-100000000000000))

    def test_edge33(self):
        self.assertRaisesRecursionError(lambda: sequence(1000000000000000))

    def test_edge34(self):
        self.assertRaisesRecursionError(lambda: sequence(-1000000000000000))

    def test_edge35(self):
        self.assertRaisesRecursionError(lambda: sequence(10000000000000000))

    def test_edge36(self):
        self.assertRaisesRecursionError(lambda: sequence(-10000000000000000))

    def test_edge37(self):
        self.assertRaisesRecursionError(lambda: sequence(100000000000000000))

    def test_edge38(self):
        self.assertRaisesRecursionError(lambda: sequence(-100000000000000000))

    def test_edge39(self):
        self.assertRaisesRecursionError(lambda: sequence(1000000000000000000))

    def test_edge40(self):
        self.assertRaisesRecursionError(lambda: sequence(-1000000000000000000))

    def test_edge41(self):
        self.assertRaisesRecursionError(lambda: sequence(10000000000000000000))

    def test_edge42(self):
        self.assertRaisesRecursionError(lambda: sequence(-10000000000000000000))

    def test_edge43(self):
        self.assertRaisesRecursionError(lambda: sequence(100000000000000000000))

    def test_edge44(self):
        self.assertRaisesRecursionError(lambda: sequence(-100000000000000000000))