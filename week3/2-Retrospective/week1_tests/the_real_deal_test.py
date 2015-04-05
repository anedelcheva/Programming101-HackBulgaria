import unittest
from the_real_deal import (sum_of_divisors, is_prime, prime_number_of_divisors,
                           contains_digit, contains_digits, is_number_balanced,
                           count_substrings, zero_insert, sum_matrix,
                           matrix_bombing_plan)


class the_real_deal_test(unittest.TestCase):

    def test_sum_of_divisors(self):
        self.assertEqual(sum_of_divisors(8), 15)
        self.assertEqual(sum_of_divisors(1), 1)
        self.assertEqual(sum_of_divisors(7), 8)
        self.assertEqual(sum_of_divisors(1000), 2340)

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(8))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(-10))

    def test_prime_number_of_divisors(self):
        self.assertTrue(prime_number_of_divisors(7))
        self.assertFalse(prime_number_of_divisors(8))
        self.assertTrue(prime_number_of_divisors(9))

    def test_contains_digit(self):
        self.assertFalse(contains_digit(123, 4))
        self.assertTrue(contains_digit(42, 2))
        self.assertTrue(contains_digit(1000, 0))
        self.assertFalse(contains_digit(12346789, 5))

    def test_contains_digits(self):
        self.assertTrue(contains_digits(402123, [0, 3, 4]))
        self.assertFalse(contains_digits(666, [6, 4]))
        self.assertFalse(contains_digits(123456789, [1, 2, 3, 0]))
        self.assertTrue(contains_digits(456, []))

    def test_is_number_balanced(self):
        self.assertTrue(is_number_balanced(9))
        self.assertTrue(is_number_balanced(11))
        self.assertFalse(is_number_balanced(13))
        self.assertTrue(is_number_balanced(121))
        self.assertTrue(is_number_balanced(4518))
        self.assertFalse(is_number_balanced(28471))
        self.assertTrue(is_number_balanced(1238033))

    def test_count_substrings(self):
        self.assertEqual(count_substrings("This is a test string", "is"), 2)
        self.assertEqual(count_substrings("babababa", "baba"), 2)
        self.assertEqual(
            count_substrings("Python is an awesome language to program in!", "o"), 4)
        self.assertEqual(
            count_substrings("We have nothing in common!", "really?"), 0)
        self.assertEqual(
            count_substrings("This is this and that is this", "this"), 2)

    def test_zerp_insert(self):
        self.assertEqual(zero_insert(116457), 10160457)
        self.assertEqual(zero_insert(55555555), 505050505050505)
        self.assertEqual(zero_insert(6446), 6040406)

    def test_sum_matrix(self):
        self.assertEqual(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)
        self.assertEqual(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)
        self.assertEqual(
            sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), 55)

    def test_matrix_bombing_plan(self):
        self.assertEqual(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         {(0, 0): 42, (0, 1): 36, (0, 2): 37, (1, 0): 30, (1, 1): 15, (1, 2): 23,
                          (2, 0): 29, (2, 1): 15, (2, 2): 26})


if __name__ == '__main__':
    unittest.main()
