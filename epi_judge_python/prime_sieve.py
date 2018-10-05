from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    sieve = [True for _ in range(n+1)]
    for i in range(2, n):
        if sieve[i]:
            curr = 2 * i
            while curr < len(sieve):
                sieve[curr] = False
                curr += i

    return [i for i in range(2, n+1) if sieve[i]]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
