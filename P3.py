#PROJECTEULER.NET PROBLEM 3. WIP


def is_prime(a):
    return all(a % i for i in xrange(2, a))

check = None
check1 = None
largestprime = 0


i = 2
while i < 600851475143:
    if is_prime(i) == True:
        if 600851475143 % i == 0:
            print i
            largestprime = i
        else:
            print i
            check = True
    i = i + 1

    
print "answer is: " + str(largestprime)

