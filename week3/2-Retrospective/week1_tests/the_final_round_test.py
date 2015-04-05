import unittest
from the_final_round import (count_words, unique_words_count, nan_expand,
                             iterations_of_nan_expand, prime_factorization,
                             group, max_consecutive, groupby, prepare_meal,
                             reduce_file_path, is_an_bn, is_credit_card_valid,
                             goldbach, magic_square, friday_years)


class the_final_round_test(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words(["apple", "banana", "apple", "pie"]),
                         {'apple': 2, 'pie': 1, 'banana': 1})
        self.assertEqual(
            count_words(["python", "python", "python", "ruby"]),
            {'ruby': 1, 'python': 3})

    def test_unique_words_count(self):
        self.assertEqual(
            unique_words_count(["apple", "banana", "apple", "pie"]), 3)
        self.assertEqual(
            unique_words_count(["python", "python", "python", "ruby"]), 2)
        self.assertEqual(unique_words_count(["HELLO!"] * 10), 1)

    def test_nan_expand(self):
        self.assertEqual(nan_expand(0), "")
        self.assertEqual(nan_expand(1), "Not a NaN")
        self.assertEqual(nan_expand(2), "Not a Not a NaN")
        self.assertEqual(nan_expand(3), "Not a Not a Not a NaN")

    def test_iterations_of_nan_expand(self):
        self.assertEqual(iterations_of_nan_expand(""), 0)
        self.assertEqual(iterations_of_nan_expand("Not a NaN"), 1)
        self.assertEqual(iterations_of_nan_expand('Not a Not a Not a Not a \
            Not a Not a Not a Not a Not a Not a NaN'), 10)
        self.assertFalse(iterations_of_nan_expand("Show these people!"))

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(10), [(2, 1), (5, 1)])
        self.assertEqual(prime_factorization(14), [(2, 1), (7, 1)])
        self.assertEqual(prime_factorization(356), [(2, 2), (89, 1)])
        self.assertEqual(prime_factorization(89), [(89, 1)])
        self.assertEqual(prime_factorization(1000), [(2, 3), (5, 3)])

    def test_group(self):
        self.assertEqual(group([1, 1, 1, 2, 3, 1, 1]),
                         [[1, 1, 1], [2], [3], [1, 1]])
        self.assertEqual(group([1, 2, 1, 2, 3, 3]),
                         [[1], [2], [1], [2], [3, 3]])

    def test_max_consecutive(self):
        self.assertEqual(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]), 4)
        self.assertEqual(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]), 3)

    def test_groupby(self):
        self.assertEqual(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]),
                         {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})
        self.assertEqual(groupby(lambda x: 'odd' if x % 2 else 'even',
                                 [1, 2, 3, 5, 8, 9, 10, 12]),
                         {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]})
        self.assertEqual(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]),
                         {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]})

    def test_prepare_meal(self):
        self.assertEqual(prepare_meal(3), "spam")
        self.assertEqual(prepare_meal(5), "eggs")
        self.assertEqual(prepare_meal(7), "")
        self.assertEqual(prepare_meal(15), "spam and eggs")
        self.assertEqual(prepare_meal(27), "spam spam spam")
        self.assertEqual(prepare_meal(45), "spam spam and eggs")

    def test_reduce_file_path(self):
        self.assertEqual(reduce_file_path("/"), "/")
        self.assertEqual(reduce_file_path("/srv/../"), "/")
        self.assertEqual(
            reduce_file_path("/srv/www/htdocs/wtf/"), "/srv/www/htdocs/wtf")
        self.assertEqual(
            reduce_file_path("/srv/www/htdocs/wtf"), "/srv/www/htdocs/wtf")
        self.assertEqual(reduce_file_path("/srv/./././././"), "/srv")
        self.assertEqual(reduce_file_path("/etc//wtf/"), "/etc/wtf")
        self.assertEqual(reduce_file_path("/etc/../etc/../etc/../"), "/")
        self.assertEqual(reduce_file_path("//////////////"), "/")
        self.assertEqual(reduce_file_path("/../"), "/")

    def test_is_an_bn(self):
        self.assertTrue(is_an_bn(""))
        self.assertFalse(is_an_bn("rado"))
        self.assertFalse(is_an_bn("aaabb"))
        self.assertTrue(is_an_bn("aaabbb"))
        self.assertFalse(is_an_bn("aabbaabb"))
        self.assertFalse(is_an_bn("bbbaaa"))
        self.assertTrue(is_an_bn("aaaaabbbbb"))

    def test_is_credit_card_valid(self):
        self.assertTrue(is_credit_card_valid(79927398713))
        self.assertFalse(is_credit_card_valid(79927398715))

    def test_goldbach(self):
        self.assertEqual(goldbach(4), [(2, 2)])
        self.assertEqual(goldbach(6), [(3, 3)])
        self.assertEqual(goldbach(8), [(3, 5)])
        self.assertEqual(goldbach(10), [(3, 7), (5, 5)])
        self.assertEqual(goldbach(100),
                         [(3, 97), (11, 89), (17, 83),
                          (29, 71), (41, 59), (47, 53)])

    def test_magic_square(self):
        self.assertFalse(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertTrue(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
        self.assertTrue(magic_square([[7, 12, 1, 14], [2, 13, 8, 11],
                                      [16, 3, 10, 5], [9, 6, 15, 4]]))
        self.assertTrue(magic_square([[23, 28, 21],
                                      [22, 24, 26], [27, 20, 25]]))
        self.assertFalse(magic_square([[16, 23, 17],
                                       [78, 32, 21], [17, 16, 15]]))

    def test_friday_years(self):
        self.assertEqual(friday_years(1000, 2000), 178)
        self.assertEqual(friday_years(1753, 2000), 44)
        self.assertEqual(friday_years(1990, 2015), 4)

if __name__ == '__main__':
    unittest.main()
