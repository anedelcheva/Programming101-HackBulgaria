import unittest
from scan_bg_web import ScanBgWeb


class ScanBgWebTest(unittest.TestCase):

    def setUp(self):
        self.bgweb = ScanBgWeb('http://register.start.bg/#b_6118')

    def test_init(self):
        self.assertTrue(isinstance(self.bgweb, ScanBgWeb))

if __name__ == '__main__':
    unittest.main()
