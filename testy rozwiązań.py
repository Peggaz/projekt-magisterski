#Funkcja odpowiedzialna za wyznaczanie liczb pierwszych
def primes(n):
    '''
    Funkcja odpowiedzialna za wyznaczanie liczb pierwszych
    @:param n - liczba do sprawdzenia
    @:return - lista liczb pierwszych
    '''
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    for x in range(2, int(n ** 0.5) + 1):
        for y in range(2, (n // x) + 1):
            sieve[(x * y)] = False
    return [i for i in range(2, n + 1) if sieve[i]]

print(primes(100))