from math import exp, log, sqrt



class IntegerFactorization:
    def __init__(self, n, base_size, attempts=1):
        self.n = n
        self.base_size = base_size
        self.attempts = attempts
        self.primes = self._generate_prime_numbers(500)


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

