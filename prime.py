n = 100
primes = [True for i in range (n+1)]
p = 2
while (p<n+1):
    if ( primes[p ]==True):
        print (p)
        for i in range (p,n+1,p):
            primes[i] = False
    p+=1