from datawiz import DW
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.dw = DW()

    def test_assertA(self):
        self.assertEqual(self.dw.get_receipt(19623631), 1)



if __name__ == '__main__':
    unittest.main()