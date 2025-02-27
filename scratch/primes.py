

def primes_method4(n):
    out = list()
    out.append(2)
    for num in range(3, n+1, 2):
        if all(num % i != 0 for i in range(2, int(num**.5 ) + 1)):
            out.append(num)
    return out

primes4 = primes_method4(2000000)
#print (primes4)
print (sum(primes4))


def primes_method5(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p] and sieve[p]%2==1):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out
primes5 = primes_method5(2000000)
print (sum(primes5))
#print (primes5)