import unittest
from github_network import GithubNetwork


class GithubNetworkTest(unittest.TestCase):

    def setUp(self):
        self.aneta = GithubNetwork('https://api.github.com/users/anedelcheva?client_id=f1a08a970e2119eab297&client_secret=b4878a1e07c7475bc65d10e6faa8d182bc593949')
        self.following = ['RadoRado', 'tborisova', 'mitko0003']

    def test_init(self):
        self.assertTrue(isinstance(self.aneta, GithubNetwork))

    def test_get_following_list(self):
        self.assertEqual(self.aneta.get_following_list(), self.following)

    def test_do_you_follow(self):
        self.assertTrue(self.aneta.do_you_follow('RadoRado'))
        self.assertTrue(self.aneta.do_you_follow('mitko0003'))
        self.assertTrue(self.aneta.do_you_follow('tborisova'))

    def test_put_connections_to_network(self):
        self.aneta.put_connections_to_network()
        relations = {
        'tborisova': [],
        'anedelcheva': ['RadoRado', 'tborisova', 'mitko0003'],
        'mitko0003': [],
        'RadoRado': []
        }
        self.assertEqual(self.aneta.network.graph, relations)


if __name__ == '__main__':
    unittest.main()
