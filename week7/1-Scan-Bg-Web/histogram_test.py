import unittest
from histogram import Histogram


class HistogramTest(unittest.TestCase):

    def setUp(self):
        self.h = Histogram()
        self.h.add('Apache')
        self.h.add('Apache')
        self.h.add('nginx')
        self.h.add('nginx')
        self.h.add('IIS')

    def test_init(self):
        self.assertTrue(isinstance(self.h, Histogram))

    def test_add(self):
        web_servers = {'Apache': 2, 'nginx': 2, 'IIS': 1}
        self.assertEqual(self.h.web_servers, web_servers)

    def test_count(self):
        self.assertEqual(self.h.count('Apache'), 2)
        self.assertEqual(self.h.count('nginx'), 2)
        self.assertEqual(self.h.count('IIS'), 1)

    def test_get_dict(self):
        web_servers = {'Apache': 2, 'nginx': 2, 'IIS': 1}
        self.assertEqual(self.h.web_servers, web_servers)

if __name__ == '__main__':
    unittest.main()
