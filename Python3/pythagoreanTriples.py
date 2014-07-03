def PythTripleGen():
    total = 3
    p = 1
    q = total - 1
    while True:
        if p >= q:
            total += 2
            p = 1
            q = total - 1
        # 1) p&q must be mutually coprime
        # 2) to find if mutually coprime, take sqrt of q,
        #   then find first prime factor that is less than p
        #   -or- check each prime factor that is less than p
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