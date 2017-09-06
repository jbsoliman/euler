#PROJECTEULER.NET PROBLEM 2 SOLUTION


s = 0
fib1 = 1
fib2 = 2
temp = 0
while fib2 < 4000000:
    if fib2 % 2 == 0:
        s = s + fib2
        temp = fib2
        fib2 = fib1 + fib2
        fib1 = temp
        
    else:
        temp = fib2
        fib2 = fib1 + fib2
        fib1 = temp
    

print "Problem 2 Solution: " + str(s)
