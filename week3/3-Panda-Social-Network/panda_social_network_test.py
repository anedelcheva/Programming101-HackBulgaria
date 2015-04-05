import unittest
from panda_social_network import PandaSocialNetwork
from panda_social_network import PandaAlreadyThere
from panda_social_network import PandasAlreadyFriends
from panda import Panda


class PandaSocialNetworkTest(unittest.TestCase):

    def setUp(self):
        self.aneta = Panda("Aneta", "aneta.nedelcheva@gmail.com", "female")
        self.pesho = Panda("Pesho", "pesho@gmail.com", "male")
        self.krisi = Panda("Krisi", "krisi@gmail.com", "female")
        self.kalin = Panda("Kalin", "kalin@gmail.com", "male")
        self.kamelia = Panda("Kamelia", "kamelia@gmail.com", "female")
        self.rado = Panda("Rado", "radorado@gmail.com", "male")
        self.iva = Panda("Iva", "iva@gmail.com", "female")
        self.maria = Panda("Maria", "maria@gmail.com", "female")
        self.nikolay = Panda("Nikolay", "nikolay@gmail.com", "male")
        self.net = PandaSocialNetwork()
        self.friends = PandaSocialNetwork()
        self.friends.make_friends(self.aneta, self.iva)
        self.friends.make_friends(self.aneta, self.rado)
        self.friends.make_friends(self.aneta, self.krisi)
        self.friends.make_friends(self.aneta, self.nikolay)
        self.friends.make_friends(self.nikolay, self.kalin)
        self.friends.make_friends(self.kalin, self.krisi)
        self.friends.make_friends(self.nikolay, self.krisi)
        self.friends.make_friends(self.pesho, self.maria)

    def test_init(self):
        self.assertTrue(isinstance(self.net, PandaSocialNetwork))

    def test_add(self):
        self.net.add(self.aneta)
        with self.assertRaises(PandaAlreadyThere):
            self.net.add(self.aneta)
        self.assertIn(self.aneta, self.net.network)

    def test_has_panda(self):
        self.assertFalse(self.net.has_panda(self.aneta))
        self.net.add(self.aneta)
        self.assertTrue(self.net.has_panda(self.aneta))

    def test_make_friends(self):
        self.net.make_friends(self.pesho, self.aneta)
        self.assertIn(self.pesho, self.net.network)
        self.assertIn(self.aneta, self.net.network)
        self.assertIn(self.pesho, self.net.network[self.aneta])
        self.assertIn(self.aneta, self.net.network[self.pesho])
        with self.assertRaises(PandasAlreadyFriends):
            self.net.make_friends(self.aneta, self.pesho)

    def test_are_friends(self):
        self.assertFalse(self.net.are_friends(self.aneta, self.pesho))
        self.net.make_friends(self.pesho, self.aneta)
        self.assertTrue(self.net.are_friends(self.aneta, self.pesho))

    def test_friends_of(self):
        self.assertFalse(self.net.friends_of(self.aneta))
        self.net.make_friends(self.aneta, self.pesho)
        self.assertEqual(self.net.network[self.aneta], [self.pesho])

    def test_connection_level(self):
        self.assertEqual(
            self.friends.connection_level(self.krisi, self.kalin), 1)
        self.assertEqual(
            self.friends.connection_level(self.aneta, self.kalin), 2)
        self.assertEqual(
            self.friends.connection_level(self.rado, self.kalin), 3)
        self.assertFalse(
            self.friends.connection_level(self.aneta, self.kamelia))
        self.assertEqual(
            self.friends.connection_level(self.pesho, self.aneta), -1)
        self.assertEqual(
            self.friends.connection_level(self.maria, self.pesho), 1)
        self.assertEqual(
            self.friends.connection_level(self.iva, self.krisi), 2)
        self.assertEqual(
            self.friends.connection_level(self.iva, self.kalin), 3)
        self.assertEqual(
            self.friends.connection_level(self.iva, self.nikolay), 2)

    def test_are_connected(self):
        self.assertTrue(self.friends.are_connected(self.krisi, self.kalin))
        self.assertTrue(self.friends.are_connected(self.aneta, self.kalin))
        self.assertTrue(self.friends.are_connected(self.rado, self.kalin))
        self.assertFalse(self.friends.are_connected(self.aneta, self.kamelia))
        self.assertFalse(self.friends.are_connected(self.pesho, self.aneta))
        self.assertTrue(self.friends.are_connected(self.maria, self.pesho))
        self.assertTrue(self.friends.are_connected(self.iva, self.krisi))
        self.assertTrue(self.friends.are_connected(self.iva, self.kalin))
        self.assertTrue(self.friends.are_connected(self.iva, self.nikolay))

    def test_how_many_gender_in_network(self):
        self.assertEqual(self.friends.how_many_gender_in_network
                         (1, self.iva, "female"), 1)
        self.assertEqual(self.friends.how_many_gender_in_network
                         (1, self.iva, "male"), 0)
        self.assertEqual(self.friends.how_many_gender_in_network
                         (2, self.iva, "female"), 2)
        self.assertEqual(self.friends.how_many_gender_in_network
                         (2, self.iva, "male"), 2)
        self.assertEqual(self.friends.how_many_gender_in_network
                         (3, self.iva, "male"), 3)
        self.assertEqual(self.friends.how_many_gender_in_network
                         (1, self.pesho, "female"), 1)
        self.assertEqual(self.friends.how_many_gender_in_network
                         (1, self.iva, "female"), 1)
        self.assertEqual(self.friends.how_many_gender_in_network
                         (1, self.maria, "female"), 0)


if __name__ == '__main__':
    unittest.main()
