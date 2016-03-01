#!/usr/bin/env python3


"""
BernoulliGenerator: Generate bernoulli random variables by flipping a fair coin
"""


__author__ = 'Ruisheng Wang'
__email__ = 'ruishenw@usc.edu'


import random
from fractions import Fraction


class BernoulliRandomVariable:

    def __init__(self, prob):
        self.p = prob   # P[X=1]=p
        self.num_flips = 0

    @staticmethod
    def _binary_expansion(p):
        p *= 2
        while p != 0:
            integral_part, fractional_part = divmod(p, 1)
            yield integral_part
            p = fractional_part * 2

    def generate_a_number(self):
        binary_expansion_p = self._binary_expansion(self.p)

        while True:
            try:
                next_bit = next(binary_expansion_p)
                coin = self._flip_a_coin()
                if coin < next_bit:
                    return 1
                elif coin > next_bit:
                    return 0
            except StopIteration:    # reach the end of binary expansion
                return 0

    def total_flips(self):
        return self.num_flips

    def _flip_a_coin(self):
        self.num_flips += 1
        return random.randint(0, 1)


def test_random_variable(p, n):

    rv = BernoulliRandomVariable(p)

    total = 0
    for _ in range(n): total += rv.generate_a_number()

    print()
    print('===================================================')
    print('P[X=1]={}'.format(p))
    print('total number of generated numbers (n): {:g}'.format(n))
    print("Arithmetic mean of generated numbers:", total/n)
    print("Average number of coin flips:", rv.total_flips()/n)
    print('===================================================')
    print()


if __name__ == '__main__':
    test_random_variable(Fraction('1/2'), 10**6)  # E[number of flips] = 1
    test_random_variable(Fraction('5/8'), 10**6)  # E[number of flips] = 1.75
    test_random_variable(Fraction('5/7'), 10**6)  # E[number of flips] = 2
