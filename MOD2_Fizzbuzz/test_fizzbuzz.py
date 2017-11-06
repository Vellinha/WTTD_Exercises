import unittest
from fizzbuzz import robot


class FizzbuzzTest(unittest.TestCase):
    def teste_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def teste_say_2_when_2(self):
        self.assertEqual(robot(2), '2')

    def teste_say_4_when_4(self):
        self.assertEqual(robot(4), '4')

    def teste_say_fizz_when_3(self):
        self.assertEqual(robot(3), 'fizz')

    def teste_say_fizz_when_6(self):
        self.assertEqual(robot(6), 'fizz')

    def teste_say_fizz_when_9(self):
        self.assertEqual(robot(9), 'fizz')

    def teste_say_fizz_when_5(self):
        self.assertEqual(robot(5), 'buzz')

    def teste_say_buzz_when_10(self):
        self.assertEqual(robot(10), 'buzz')

    def teste_say_fizz_when_20(self):
        self.assertEqual(robot(20), 'buzz')

    def teste_say_fizz_when_15(self):
        self.assertEqual(robot(15), 'fizzbuzz')

    def teste_say_fizz_when_30(self):
        self.assertEqual(robot(30), 'fizzbuzz')

    def teste_say_fizz_when_45(self):
        self.assertEqual(robot(45), 'fizzbuzz')
