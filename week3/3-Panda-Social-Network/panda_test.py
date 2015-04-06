import unittest
from panda import Panda


class PandaTest(unittest.TestCase):

    def setUp(self):
        self.my_panda = Panda("Aneta", "aneta.nedelcheva@gmail.com", "female")

    def test_init(self):
        self.assertTrue(isinstance(self.my_panda, Panda))
        with self.assertRaises(ValueError):
            Panda("Aneta", "aneta.nedelchevagmail.com", "female")
        with self.assertRaises(ValueError):
            Panda("Aneta", "aneta.nedelcheva@gmailcom", "female")

    def test_get_name(self):
        self.assertEqual(self.my_panda.name, self.my_panda.get_name())

    def test_get_email(self):
        self.assertEqual(self.my_panda.email, self.my_panda.get_email())

    def test_get_gender(self):
        self.assertEqual(self.my_panda.gender, self.my_panda.get_gender())

    def test_isMale(self):
        self.assertFalse(self.my_panda.isMale())

    def test_isFemale(self):
        self.assertTrue(self.my_panda.isFemale())

    def test_eq(self):
        self.your_panda = Panda(
            "Aneta", "aneta.nedelcheva@gmail.com", "female")
        self.assertTrue(self.my_panda == self.your_panda)

    def test_str(self):
        aneta = "Panda Aneta with email aneta.nedelcheva@gmail.com and female gender."
        self.assertEqual(str(self.my_panda), aneta)

    def test_repr(self):
        self.assertEqual(repr(self.my_panda),
                         "Panda('Aneta', 'aneta.nedelcheva@gmail.com', 'female')")

    def test_hash(self):
        self.assertIsNotNone(hash(self.my_panda))


if __name__ == '__main__':
    unittest.main()
