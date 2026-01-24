import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(8))

    def test_edge(self):
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))

    def test_edge2(self):
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))

    def test_edge3(self):
        self.assertFalse(is_not_prime(11))
        self.assertFalse(is_not_prime(13))

    def test_edge4(self):
        self.assertFalse(is_not_prime(23))
        self.assertFalse(is_not_prime(29))

    def test_edge5(self):
        self.assertFalse(is_not_prime(37))
        self.assertFalse(is_not_prime(41))

    def test_edge6(self):
        self.assertFalse(is_not_prime(53))
        self.assertFalse(is_not_prime(59))

    def test_edge7(self):
        self.assertFalse(is_not_prime(71))
        self.assertFalse(is_not_prime(73))

    def test_edge8(self):
        self.assertFalse(is_not_prime(79))
        self.assertFalse(is_not_prime(83))

    def test_edge9(self):
        self.assertFalse(is_not_prime(89))
        self.assertFalse(is_not_prime(97))

    def test_edge10(self):
        self.assertFalse(is_not_prime(101))
        self.assertFalse(is_not_prime(103))

    def test_edge11(self):
        self.assertFalse(is_not_prime(107))
        self.assertFalse(is_not_prime(109))

    def test_edge12(self):
        self.assertFalse(is_not_prime(113))
        self.assertFalse(is_not_prime(127))

    def test_edge13(self):
        self.assertFalse(is_not_prime(131))
        self.assertFalse(is_not_prime(137))

    def test_edge14(self):
        self.assertFalse(is_not_prime(139))
        self.assertFalse(is_not_prime(149))

    def test_edge15(self):
        self.assertFalse(is_not_prime(151))
        self.assertFalse(is_not_prime(157))

    def test_edge16(self):
        self.assertFalse(is_not_prime(163))
        self.assertFalse(is_not_prime(167))

    def test_edge17(self):
        self.assertFalse(is_not_prime(173))
        self.assertFalse(is_not_prime(179))

    def test_edge18(self):
        self.assertFalse(is_not_prime(181))
        self.assertFalse(is_not_prime(191))

    def test_edge19(self):
        self.assertFalse(is_not_prime(193))
        self.assertFalse(is_not_prime(197))

    def test_edge20(self):
        self.assertFalse(is_not_prime(199))
        self.assertFalse(is_not_prime(211))

    def test_edge21(self):
        self.assertFalse(is_not_prime(223))
        self.assertFalse(is_not_prime(227))

    def test_edge22(self):
        self.assertFalse(is_not_prime(229))
        self.assertFalse(is_not_prime(233))

    def test_edge23(self):
        self.assertFalse(is_not_prime(239))
        self.assertFalse(is_not_prime(241))

    def test_edge24(self):
        self.assertFalse(is_not_prime(251))
        self.assertFalse(is_not_prime(257))

    def test_edge25(self):
        self.assertFalse(is_not_prime(263))
        self.assertFalse(is_not_prime(269))

    def test_edge26(self):
        self.assertFalse(is_not_prime(271))
        self.assertFalse(is_not_prime(277))

    def test_edge27(self):
        self.assertFalse(is_not_prime(281))
        self.assertFalse(is_not_prime(283))

    def test_edge28(self):
        self.assertFalse(is_not_prime(293))
        self.assertFalse(is_not_prime(299))

    def test_edge29(self):
        self.assertFalse(is_not_prime(307))
        self.assertFalse(is_not_prime(311))

    def test_edge30(self):
        self.assertFalse(is_not_prime(313))
        self.assertFalse(is_not_prime(317))

    def test_edge31(self):
        self.assertFalse(is_not_prime(331))
        self.assertFalse(is_not_prime(337))

    def test_edge32(self):
        self.assertFalse(is_not_prime(347))
        self.assertFalse(is_not_prime(349))

    def test_edge33(self):
        self.assertFalse(is_not_prime(353))
        self.assertFalse(is_not_prime(359))

    def test_edge34(self):
        self.assertFalse(is_not_prime(367))
        self.assertFalse(is_not_prime(373))

    def test_edge35(self):
        self.assertFalse(is_not_prime(379))
        self.assertFalse(is_not_prime(383))

    def test_edge36(self):
        self.assertFalse(is_not_prime(389))
        self.assertFalse(is_not_prime(397))

    def test_edge37(self):
        self.assertFalse(is_not_prime(401))
        self.assertFalse(is_not_prime(409))

    def test_edge38(self):
        self.assertFalse(is_not_prime(419))
        self.assertFalse(is_not_prime(421))

    def test_edge39(self):
        self.assertFalse(is_not_prime(431))
        self.assertFalse(is_not