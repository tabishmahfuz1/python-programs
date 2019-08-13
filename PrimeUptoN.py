import math

def printPrimeNumbers(N):
    print(2, " ")
    for i in range(3, N + 1):
        isPrime = True;
        for j in range(2, int(math.sqrt(i)) + 1):
            if(i % j == 0):
                isPrime = False
                break
        if(isPrime):
            print(i, " ")
    
number = int(input())
printPrimeNumbers(number)

# Write your code here
import math

# def printPrimeNumbers(N):
    # print(2, end =" ")
    # for i in range(3, N + 1, 2):
        # isPrime = True;
        # for j in range(3, int(math.sqrt(i)) + 1, 2):
            # if(i % j == 0):
                # isPrime = False
                # break
        # if(isPrime):
            # print(i, end =" ")
    
# number = int(input())
# printPrimeNumbers(number)