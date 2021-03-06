import unittest
from warmups import (factorial, fibonacci, sum_of_digits, fact_digits, palindrome, to_digits,
                     to_number, fib_number, count_vowels, count_consonants,
                     char_histogram, p_score, is_increasing, is_decreasing,
                     next_hack)


class fact_digits_test(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(0), 1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), [1])
        self.assertEqual(fibonacci(2), [1, 1])
        self.assertEqual(fibonacci(3), [1, 1, 2])
        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(1325132435356), 43)
        self.assertEqual(sum_of_digits(6), 6)
        self.assertEqual(sum_of_digits(-10), 1)

    def test_fact_digits(self):
        self.assertEqual(fact_digits(111), 3)
        self.assertEqual(fact_digits(145), 145)
        self.assertEqual(fact_digits(999), 1088640)

    def test_panindrome(self):
        self.assertTrue(palindrome(121))
        self.assertTrue(palindrome("kapak"))
        self.assertFalse(palindrome("baba"))

    def test_to_digits(self):
        self.assertEqual(to_digits(123), [1, 2, 3])
        self.assertEqual(to_digits(99999), [9, 9, 9, 9, 9])
        self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_to_number(self):
        self.assertEqual(to_number([1, 2, 3]), 123)
        self.assertEqual(to_number([9, 9, 9, 9, 9]), 99999)
        self.assertEqual(to_number([1, 2, 0, 2, 3]), 12023)

    def test_fib_number(self):
        self.assertEqual(fib_number(3), 112)
        self.assertEqual(fib_number(10), 11235813213455)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Python"), 2)
        self.assertEqual(count_vowels("Theistareykjarbunga"), 8)
        self.assertEqual(count_vowels("grrrrgh"), 0)
        self.assertEqual(count_vowels("Github is the second best thing that \
            happened to programmers, after the keyboard!"), 23)
        self.assertEqual(count_vowels("A nice day to code!"), 8)

    def test_count_consonants(self):
        self.assertEqual(count_consonants("Python"), 4)
        self.assertEqual(count_consonants("Theistareykjarbunga"), 11)
        self.assertEqual(count_consonants("grrrrgh!"), 7)
        self.assertEqual(count_consonants("Github is the second best thing that \
            happened to programmers, after the keyboard!"), 44)
        self.assertEqual(count_consonants("A nice day to code!"), 6)

    def test_char_histogram(self):
        self.assertEqual(char_histogram(
            "Python!"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})
        self.assertEqual(
            char_histogram("AAAAaaa!!!"), {'A': 4, 'a': 3, "!": 3})

    def test_p_score(self):
        self.assertEqual(p_score(121), 1)
        self.assertEqual(p_score(48), 3)
        self.assertEqual(p_score(198), 6)

    def test_ia_increasing(self):
        self.assertTrue(is_increasing([1, 2, 3, 4, 5]))
        self.assertTrue(is_increasing([1]))
        self.assertFalse(is_increasing([5, 6, -10]))
        self.assertFalse(is_increasing([1, 1, 1, 1]))

    def test_is_decreasing(self):
        self.assertTrue(is_decreasing([5, 4, 3, 2, 1]))
        self.assertFalse(is_decreasing([1, 2, 3]))
        self.assertTrue(is_decreasing([100, 50, 20]))
        self.assertFalse(is_decreasing([1, 1, 1, 1]))

    def test_next_hack(self):
        self.assertEqual(next_hack(0), 1)
        self.assertEqual(next_hack(10), 21)
        self.assertEqual(next_hack(8031), 8191)


if __name__ == '__main__':
    unittest.main()
