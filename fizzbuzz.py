import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_divisible_by_3_returns_fizz(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.take(3)
        self.assertEqual(result, "fizz")

    def test_divisible_by_5_returns_buzz(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.take(5)
        self.assertEqual(result, "buzz")

    def test_not_divisible_by_3_or_5_returns_number(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.take(4)
        self.assertEqual(result, 4)


class FizzBuzz:
    def take(self, number):
        if number % 3 == 0:
            return 'fizz'
        elif number % 5 == 0:
            return 'buzz'
        else:
            return number


if __name__ == '__main__':
    unittest.main()
