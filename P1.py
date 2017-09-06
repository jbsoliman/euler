#PROJECTEULER.NET PROBLEM 1 SOLUTION

s = 0

for i in range(0,1000):
    if i % 3 == 0 or  i % 5 == 0:
        s = s + i

print "Problem 1 Solution: " + str(s)
