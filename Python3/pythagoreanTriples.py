from math import sqrt
from math import floor

def isPrime(num):
    if num > 1:
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, num, 2):
            if num % i == 0:
                return False
        return True
    return False

def nextPrime(num):
    while True:
        if isPrime(num):
            return num
        num += 1

def PythTripleGen():
    total = 3
    p = 1
    q = total - 1
    while True:
        if p >= q:
            total += 2 # skip sums of p & q that are even
            p = 1
            q = total - 1
        # 1) p&q must be mutually coprime
        # 2) to find if mutually coprime, take sqrt of q,
        #   then find first prime factor that is less than p
        #   -or- check each prime factor that is less than p
        primediv = floor(sqrt(q))
        
            
        yield q**2 - p**2, 2*q*p, p**2 + q**2
        p += 1
        q = total - p

if __name__ == '__main__':
    query = "T to generate the next triple, Q to quit: "
    thisGen = PythTripleGen()
    while True:        
        response = input(query)
        if response == 't' or response == 'T':
            print(sorted(next(thisGen)))
        elif response == 'q' or response == 'Q':
            break