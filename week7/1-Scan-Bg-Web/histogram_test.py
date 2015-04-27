import unittest
from histogram import Histogram


class HistogramTest(unittest.TestCase):

    def setUp(self):
        self.h = Histogram()

    def test_init(self):
        self.assertTrue(isinstance(self.h, Histogram))

    def test_add(self):
        self.h.add('Apache')
        self.h.add('Apache')
        self.h.add('nginx')
        self.h.add('nginx')
        self.h.add('IIS')
        web_servers = {'Apache': 2, 'nginx': 2, 'IIS': 1}
        self.assertEqual(self.h.web_servers, web_servers)

    def test_count(self):
        self.h.add('Apache')
        self.h.add('Apache')
        self.h.add('nginx')
        self.h.add('nginx')
        self.h.add('IIS')
        self.assertEqual(self.h.count('Apache'), 2)
        self.assertEqual(self.h.count('nginx'), 2)
        self.assertEqual(self.h.count('IIS'), 1)

    def test_get_dict(self):
        web_servers = {'Apache': 0, 'nginx': 0, 'IIS': 0}
        self.assertEqual(self.h.web_servers, web_servers)

if __name__ == '__main__':
    unittest.main()
