import unittest


class FizzBuzzTest(uniitest.TestCase):
    def test_divisisble_by_3_should_return_fizz(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.take(3)
        self.assertEqual(result, 3)


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
