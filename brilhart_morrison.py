from math import exp, log, sqrt
import numpy as np
import time
from itertools import chain


class IntegerFactorization:
    def __init__(self, n, base_size, attempts=1):
        self.n = n
        self.base_size = base_size
        self.attempts = attempts
        self.primes = self._generate_prime_numbers(500)
        self.factor_base = self._build_factor_base()

    @staticmethod
    def _littlewood_function(n):

        return exp(sqrt(log(n) * log(log(n))))

    @staticmethod
    def _legendre_symbol(a, p):

        return pow(a, (p - 1) // 2, p)

    @staticmethod
    def _sieve_eratosthenes(limit):

        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for start in range(2, int(limit ** 0.5) + 1):
            if sieve[start]:
                for multiple in range(start * start, limit + 1, start):
                    sieve[multiple] = False
        return [num for num, is_prime in enumerate(sieve) if is_prime]

    def _generate_prime_numbers(self, count):

        limit = 1000
        primes = self._sieve_eratosthenes(limit)
        while len(primes) < count:
            limit *= 2
            primes = self._sieve_eratosthenes(limit)
        return primes[:count]

    @staticmethod
    def _gauss_mod2(matrix):

        matrix = np.mod(matrix, 2)
        num_rows, num_cols = matrix.shape
        marked_rows = set()
        for col in range(num_cols):
            row = next((r for r in range(num_rows) if matrix[r, col] != 0), None)
            if row is not None:
                marked_rows.add(row)
                for k in chain(range(col), range(col + 1, num_cols)):
                    if matrix[row, k] == 1:
                        matrix[:, k] = (matrix[:, col] + matrix[:, k]) % 2
        for row in range(num_rows):
            if row not in marked_rows and any(matrix[row]):
                solution = np.zeros(num_rows, dtype=bool)
                solution[row] = True
                vector = matrix[row]
                for l in chain(range(row), range(row + 1, num_rows)):
                    if (matrix[l] & vector).any():
                        solution[l] = True
                        vector = (vector + matrix[l]) % 2
                    if not any(vector):
                        yield solution
                        break

    def _factor_base_representation(self, b):

        n = self.n
        k = self.factor_base.shape[0]
        pows = np.zeros(k, dtype=np.int64)
        i = 0
        if self.factor_base[i] == -1:
            if (t := -b % n) != 0 and t < b:
                pows[i] = 1
            i += 1

        while i < k:
            e = self.factor_base[i]
            while b % e == 0:
                pows[i] += 1
                b //= e
            i += 1

        if b != 1:
            return None
        return pows

    def _continued_fractions(self):

        n = self.n
        m = sqrt(n)
        v = 1
        alpha = m
        a = int(alpha)
        u = a
        preprev = 0
        prev = 1
        while True:
            ret = a * prev + preprev
            preprev = prev
            prev = ret
            yield ret
            v = (n - u ** 2) // v
            alpha = (m + u) / v
            a = int(alpha)
            u = a * v - u

    def _build_factor_base(self):

        factor_base = [-1]
        for prime in self.primes:
            if len(factor_base) >= self.base_size or prime > np.power(self._littlewood_function(self.n), 1 / np.sqrt(2)):
                break
            if self._legendre_symbol(self.n, prime) == 1:
                factor_base.append(prime)
        return np.array(factor_base, dtype=int)

    def factorize(self):

        factor_base = self.factor_base
        k = len(factor_base)
        cfrac_gen = self._continued_fractions()

        for _ in range(self.attempts):
            p = 0
            a_b_smooth = np.zeros(k + 1, dtype=np.int64)
            v = np.zeros((k + 1, k), dtype=np.int64)
            while p != k + 1:
                a = next(cfrac_gen) % self.n
                b = (a ** 2) % self.n
                if (c := self._factor_base_representation(b)) is not None:
                    v[p] = c
                    a_b_smooth[p] = a
                    p += 1

            solutions = self._gauss_mod2(v)

            for solution in solutions:
                x = 1
                for xi in np.power(a_b_smooth, solution):
                    x = x * int(xi) % self.n
                y = 1
                for yi in np.power(factor_base, np.sum(np.multiply(solution, v.transpose()).transpose(), 0) // 2):
                    y = y * int(yi) % self.n

                if x == y or x == (-y % self.n):
                    continue
                return int(np.gcd(x + y, self.n)), int(np.gcd(x - y, self.n))

        return None


