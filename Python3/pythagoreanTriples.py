from fractions import gcd

def PythTripleGen():
    total = 3
    p = 1
    q = total - 1
    while True:
        if p >= q:
            total += 2 # skip sums of p & q that are even
            p = 1
            q = total - 1
        if gcd(p, q) == 1: # check that p & q are coprime
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